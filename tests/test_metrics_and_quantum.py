"""Numerical metrics and Qiskit circuit contract tests."""

import numpy as np
import pytest
from qiskit.quantum_info import Statevector

from certiq_chirp.metrics import clip, metric_bundle
from certiq_chirp.stage1_hybrid import quantum_kernel, quantum_states
from certiq_chirp.stage2_qaoa import build_qaoa_circuit
from certiq_chirp.stage3_bernoulli import (
    build_bernoulli_circuit,
    poisson_binomial_at_least,
    stage3_circuit,
)


@pytest.mark.filterwarnings("ignore:.*disp.*iprint.*:DeprecationWarning")
def test_metric_bundle_and_probability_clipping_are_finite():
    y = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0])
    p = np.array([-1.0, 0.8, 0.2, 0.7, 0.1, 0.3, 0.9, 0.4, 0.6, 2.0])
    clipped = clip(p)
    assert clipped.min() >= 1e-6
    assert clipped.max() <= 1 - 1e-6
    metrics = metric_bundle(y, clipped)
    assert 0 <= metrics["roc_auc"] <= 1
    assert 0 <= metrics["pr_auc"] <= 1
    assert metrics["k_top"] == 1


def test_four_qubit_quantum_kernel_is_normalized_symmetric_and_psd():
    angles = np.array(
        [
            [0.0, 0.2, 0.4, 0.6],
            [0.8, 1.0, 1.2, 1.4],
            [1.5, 1.2, 0.9, 0.6],
        ]
    )
    states = quantum_states(angles)
    kernel = quantum_kernel(states, states)

    assert states.shape == (3, 16)
    assert kernel.shape == (3, 3)
    np.testing.assert_allclose(np.diag(kernel), np.ones(3), atol=1e-12)
    np.testing.assert_allclose(kernel, kernel.T, atol=1e-12)
    assert np.linalg.eigvalsh(kernel).min() >= -1e-10


def test_ten_qubit_qaoa_circuit_has_expected_layers_and_gates():
    n_qubits = 10
    diagonal = np.linspace(-1.0, 1.0, 2**n_qubits)
    circuit = build_qaoa_circuit(
        n_qubits,
        diagonal,
        params=[0.1, 0.2, 0.3, 0.4],
        p_layers=2,
    )

    assert circuit.num_qubits == 10
    assert circuit.count_ops()["ry"] == 10
    assert circuit.count_ops()["diagonal"] == 2
    assert circuit.count_ops()["rx"] == 20
    assert circuit.num_clbits == 0


def test_six_qubit_bernoulli_circuit_matches_poisson_binomial_reference():
    probabilities = np.array([0.45, 0.43, 0.42, 0.33, 0.33, 0.32])
    circuit, angles = build_bernoulli_circuit(probabilities)
    exact = poisson_binomial_at_least(probabilities, threshold=3)
    state = Statevector.from_instruction(circuit)
    statevector_tail = sum(
        probability
        for index, probability in enumerate(state.probabilities())
        if index.bit_count() >= 3
    )

    assert circuit.num_qubits == 6
    assert len(angles) == 6
    assert circuit.count_ops()["ry"] == 6
    assert circuit.count_ops().get("cx", 0) == 0
    np.testing.assert_allclose(statevector_tail, exact, atol=1e-12)


def test_stage3_simulation_returns_finite_reference_and_noise_diagnostics():
    probabilities = np.array([0.45, 0.43, 0.42, 0.33, 0.33, 0.32])
    result = stage3_circuit(probabilities, shots=2048)

    assert result["logical_qubits"] == 6
    assert result["logical_depth"] == 1
    assert result["two_qubit_gates"] == 0
    assert sum(result["noiseless_counts"].values()) == 2048
    assert sum(result["noisy_counts"].values()) == 2048
    np.testing.assert_allclose(
        result["ideal_statevector_probability"],
        result["exact_analytical_probability"],
        atol=1e-12,
    )
    assert all(0 <= result[name] <= 1 for name in (
        "exact_analytical_probability",
        "noiseless_finite_shot_probability",
        "monte_carlo_probability",
        "noisy_probability",
        "mitigated_probability",
    ))
