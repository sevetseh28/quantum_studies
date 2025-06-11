from qiskit import QuantumCircuit, execute
from qiskit.providers.basicaer import BasicAer
qc = QuantumCircuit(3, 3) # Create a 3-qubit, 3-classical bit circuit
qc.h([1, 2])  # Apply Hadamard gate to qubits 1 and 2
qc.x(0)

# Measure all qubits specifying classical bits
qc.measure([0, 1, 2], [0, 1, 2])  # Measure qubits 0, 1, and 2 into classical bits 0, 1, and 2

qc.measure(0, 0)  # Measure qubit 0 into classical bit 0
qc.measure(1, 1)  # Measure qubit 1 into classical bit 1
qc.measure(2, 2)  # Measure qubit 2 into classical bit 2

qc.measure([0, 1], [0, 1])  # Measure qubits 0 and 1 into classical bits 0 and 1, leaving classical bit 2 unused

# We can also use measure_all() for convenience
# qc.measure_all() # Creates a barrier and three classical bits for each qubit ) # This also creates a new classical register with three bits apart from the original classical register

print(qc.draw())  # Visualize the circuit

job = execute(qc, backend=BasicAer.get_backend('qasm_simulator'), shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)  # Print the measurement results