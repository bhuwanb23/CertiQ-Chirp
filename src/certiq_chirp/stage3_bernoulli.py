"""Six-qubit Bernoulli ledger, noisy simulation, and mitigation."""

import numpy as np
from scipy.optimize import nnls
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError

from .config import SEEDS, SHOTS


def poisson_binomial_at_least(ps, threshold=3):
    dp = np.zeros(len(ps) + 1); dp[0] = 1.0
    for p in ps:
        nxt = np.zeros_like(dp)
        for k in range(len(dp)):
            nxt[k] += dp[k] * (1 - p)
            if k + 1 < len(dp): nxt[k + 1] += dp[k] * p
        dp = nxt
    return float(dp[threshold:].sum())


def bit_success(counts, threshold=3):
    total = 0; success = 0
    for key, val in counts.items():
        key = str(key).replace(" ", "")
        total += int(val)
        if key.count("1") >= threshold: success += int(val)
    return success / max(1, total)


def qiskit_counts_index(key, n):
    """Convert Qiskit c[n-1]...c0 key into an integer with q0 as LSB."""
    key = str(key).replace(" ", "")
    return sum((1 << i) for i, bit in enumerate(key[::-1]) if bit == "1")


def noise_response_matrix(n, depol, readout):
    """P(measured bitstring | ideal bitstring) for depolarizing + symmetric readout."""
    dim = 2 ** n
    M = np.zeros((dim, dim))
    for z in range(dim):
        p1 = []
        for i in range(n):
            b = (z >> i) & 1
            after_depol = (1 - depol) * b + depol / 2
            p1.append(readout + (1 - 2 * readout) * after_depol)
        for m in range(dim):
            pr = 1.0
            for i in range(n):
                pr *= p1[i] if (m >> i) & 1 else (1 - p1[i])
            M[m, z] = pr
    return M


def build_bernoulli_circuit(ps):
    """Encode independent Bernoulli probabilities using one RY gate per qubit."""
    n = len(ps)
    qc = QuantumCircuit(n)
    angles = [2 * np.arcsin(np.sqrt(float(p))) for p in ps]
    for i, theta in enumerate(angles): qc.ry(theta, i)
    return qc, angles


def stage3_circuit(ps, shots=SHOTS):
    n = len(ps)
    qc, angles = build_bernoulli_circuit(ps)
    qc_meas = qc.copy(); qc_meas.measure_all()
    sv = Statevector.from_instruction(qc)
    probs = sv.probabilities()
    p_statevector = float(sum(probs[i] for i in range(2 ** n) if i.bit_count() >= 3))
    p_exact = poisson_binomial_at_least(ps, 3)

    noiseless = AerSimulator(seed_simulator=SEEDS["simulator"])
    counts_ideal = noiseless.run(transpile(qc_meas, noiseless), shots=shots,
                                 seed_simulator=SEEDS["simulator"]).result().get_counts()
    p_ideal = bit_success(counts_ideal, 3)

    depol = 0.02; readout = 0.03
    noise = NoiseModel()
    noise.add_all_qubit_quantum_error(depolarizing_error(depol, 1), ["ry"])
    noise.add_all_qubit_readout_error(ReadoutError([[1-readout, readout], [readout, 1-readout]]))
    noisy_sim = AerSimulator(noise_model=noise, seed_simulator=SEEDS["simulator"] + 1)
    tqc_noisy = transpile(qc_meas, basis_gates=noise.basis_gates, optimization_level=0)
    counts_noisy = noisy_sim.run(tqc_noisy, shots=shots,
                                 seed_simulator=SEEDS["simulator"] + 1).result().get_counts()
    p_noisy = bit_success(counts_noisy, 3)

    # Full 64x64 response-matrix unfolding with non-negative least squares.
    observed = np.zeros(2 ** n)
    total = sum(int(v) for v in counts_noisy.values())
    for key, val in counts_noisy.items():
        observed[qiskit_counts_index(key, n)] += int(val) / total
    R = noise_response_matrix(n, depol, readout)
    A = np.vstack([R, 10.0 * np.ones((1, 2 ** n))])
    b = np.concatenate([observed, np.array([10.0])])
    unfolded, _ = nnls(A, b)
    unfolded = unfolded / unfolded.sum()
    p_mitigated_full = float(sum(unfolded[i] for i in range(2 ** n) if i.bit_count() >= 3))

    # Primary mitigation: invert the known noise channel on six marginals, then
    # recompute the exact Poisson-binomial tail. This is statistically more
    # efficient than unfolding all 64 bins at 32,768 shots.
    marginals = np.array([sum(observed[i] for i in range(2 ** n) if (i >> q) & 1) for q in range(n)])
    pre_readout = (marginals - readout) / (1 - 2 * readout)
    mitigated_ps = np.clip((pre_readout - depol / 2) / (1 - depol), 0, 1)
    p_mitigated = poisson_binomial_at_least(mitigated_ps, 3)

    rng = np.random.default_rng(SEEDS["monte_carlo"])
    mc = rng.random((shots, n)) < np.asarray(ps)
    p_mc = float((mc.sum(axis=1) >= 3).mean())

    tqc = transpile(qc, basis_gates=["u", "cx"], optimization_level=1)
    ops = tqc.count_ops()
    one_q = sum(int(v) for k, v in ops.items() if k in {"u", "u1", "u2", "u3", "ry", "rz", "sx", "x", "h"})
    two_q = int(ops.get("cx", 0))
    return {
        "qubit_order": [f"q{i}" for i in range(n)],
        "bit_order_note": "Qiskit printed keys are c5...c0; q0 is the rightmost character. Hamming weight is order-invariant.",
        "input_probabilities": [float(p) for p in ps],
        "ry_angles": [float(a) for a in angles],
        "exact_analytical_probability": p_exact,
        "ideal_statevector_probability": p_statevector,
        "noiseless_finite_shot_probability": p_ideal,
        "monte_carlo_probability": p_mc,
        "noisy_probability": p_noisy,
        "mitigated_probability": float(p_mitigated),
        "response_matrix_mitigated_probability": float(p_mitigated_full),
        "mitigation_method": "noise-model-aware marginal inversion; 64x64 NNLS response-matrix cross-check",
        "errors": {
            "finite_shot_vs_exact": float(abs(p_ideal - p_exact)),
            "monte_carlo_vs_exact": float(abs(p_mc - p_exact)),
            "noisy_vs_exact": float(abs(p_noisy - p_exact)),
            "mitigated_vs_exact": float(abs(p_mitigated - p_exact)),
            "response_matrix_mitigated_vs_exact": float(abs(p_mitigated_full - p_exact)),
        },
        "finite_shot_standard_error": float(np.sqrt(p_exact * (1 - p_exact) / shots)),
        "finite_shot_ci95_half_width": float(1.96 * np.sqrt(p_exact * (1 - p_exact) / shots)),
        "shots": shots,
        "noise_model": {"single_qubit_depolarizing": depol, "symmetric_readout_error": readout},
        "logical_qubits": n,
        "logical_depth": int(qc.depth()),
        "transpiled_depth": int(tqc.depth()),
        "one_qubit_gates": int(one_q),
        "two_qubit_gates": two_q,
        "swap_gates": int(ops.get("swap", 0)),
        "transpiled_ops": {k: int(v) for k, v in ops.items()},
        "noiseless_counts": {str(k): int(v) for k, v in counts_ideal.items()},
        "noisy_counts": {str(k): int(v) for k, v in counts_noisy.items()},
    }
