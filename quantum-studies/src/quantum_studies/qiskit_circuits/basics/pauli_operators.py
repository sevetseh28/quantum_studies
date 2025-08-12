from qiskit.quantum_info import Pauli
from qiskit import QuantumCircuit


p = Pauli('IZ') # IZ pauli operator represents an Operator on a 2-qubit 
print("Pauli operator:\n", p.to_matrix())

qc = QuantumCircuit(2)
qc.unitary(p.to_matrix(), [0, 1], label='IZ From Pauli')  # Apply the Pauli operator to the circuit

qc.pauli("IZ", [0, 1])  # Apply the Pauli operator to the circuit

print(qc.draw())