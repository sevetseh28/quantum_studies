
from qiskit.circuit.library import CCXGate
from qiskit import QuantumCircuit


qc = QuantumCircuit(3)  # Create a quantum circuit with 3 qubits
# qc.ccx(0, 1, 2)  # Apply the Toffoli gate (CCX) on qubits 0, 1, and 2
# qc.toffoli(0, 1, 2)  # Another way to apply the Toffoli gate

toffoli_gate = CCXGate()

print(toffoli_gate.definition.draw())