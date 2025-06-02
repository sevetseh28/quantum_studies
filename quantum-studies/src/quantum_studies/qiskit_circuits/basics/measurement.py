from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 3) # Create a 3-qubit, 3-classical bit circuit
qc.h([0, 1, 2])  # Apply Hadamard gate to all qubits

# Measure all qubits specifying classical bits
# qc.measure([0, 1, 2], [0, 1, 2])  # Measure qubits 0, 1, and 2 into classical bits 0, 1, and 2

# We can also use measure_all() for convenience
# qc.measure_all() # Creates a barrier and three classical bits for each qubit ) # This also creates a new classical register with three bits apart from the original classical register

print(qc.draw())  # Visualize the circuit