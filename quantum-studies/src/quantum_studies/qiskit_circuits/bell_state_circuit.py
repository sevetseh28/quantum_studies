from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit import transpile

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to qubit 0 (puts it into superposition)
qc.h(0)

# Apply a CNOT gate (entangles qubit 0 and 1)
qc.cx(0, 1)

# Measure both qubits into classical bits
qc.measure(0, 0)
qc.measure(1, 1)

# Visualize the circuit
print(qc.draw())

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

counts = result.get_counts()
print("Measurement results:", counts)