from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate, C3XGate


mcx_gate = MCXGate(3)

qc = QuantumCircuit(4)
qc.append(mcx_gate, [0, 1, 2, 3])  # Append the MCX gate to the circuit
print(qc.draw())  # Visualize the circuit

qc.barrier(0, 1) # Arguments works
qc.barrier([1, 2]) # List also works

qc.append(C3XGate(), [0, 1, 2, 3])  # Append the C3X gate to the circuit
print(qc.draw())  # Visualize the circuit