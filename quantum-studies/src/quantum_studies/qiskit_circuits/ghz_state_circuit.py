from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator

# Create a 3-qubit, 3-classical bit circuit
qc = QuantumCircuit(3, 3)

# Step 1: Hadamard on qubit 0
qc.h(0)

# Step 2: CNOT from qubit 0 to qubit 1
qc.cx(0, 1)

# Step 3: CNOT from qubit 0 to qubit 2
qc.cx(0, 2)

# Step 4: Measure all qubits
qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()
counts = result.get_counts()
print("Measurement results:", counts)
