from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import Aer


# Create a 3-qubit, 3-classical bit circuit
qc = QuantumCircuit(3, 3)

# I'll create a circuit that generates a GHZ state (Greenberger-Horne-Zeilinger state)

# Step 1: Hadamard on qubit 0 - Superposition
qc.h(0)

# Step 2: CNOT from qubit 0 to qubit 1 - Entanglement
qc.cx(0, 1)

# Step 3: CNOT from qubit 0 to qubit 2 - Further entanglement
qc.cx(0, 2)

# Doing this will also create a GHZ  cx.([0, 1], [1, 2])

# Step 4: Measure all qubits
qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
qasm_simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, shots=1024, backend=qasm_simulator).result()
counts = result.get_counts()
print("Measurement results:", counts)
