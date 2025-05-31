
from qiskit.circuit import QuantumCircuit, ParameterVector
import math
theta = ParameterVector("θ", 3)  # Create a vector of parameters
qc = QuantumCircuit(3)

qc.h([0, 1, 2])  # Apply Hadamard gate to all qubits
qc.p(theta[0], 0)  # Apply phase shift to qubit 0
qc.p(theta[1], 1)  # Apply phase shift to qubit 1
qc.p(theta[2], 2)  # Apply phase shift to qubit 2

print(qc.draw())  # Visualize the circuit
# Note: The circuit is parametrized with three phase shifts, one for each qubit.

b_qc = qc.assign_parameters({theta: [math.pi / 8, math.pi / 4, math.pi /2]})

print(b_qc.draw())  # Visualize the circuit with bound parameters