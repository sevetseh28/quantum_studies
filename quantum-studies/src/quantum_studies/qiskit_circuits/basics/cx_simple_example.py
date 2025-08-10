from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.h(0)  # Apply Hadamard gate to qubit 0
qc.cx(0, 1)  # Apply CNOT gate (entangles qubit 0 and 1)
qc.cx(0, 2)  # Apply CNOT gate (entangles qubit 0 and 2)
print(qc.draw())  # Visualize the circuit