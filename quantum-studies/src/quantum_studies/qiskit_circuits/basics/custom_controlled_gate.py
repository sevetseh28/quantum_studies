from qiskit import QuantumCircuit
import math


p16_qc = QuantumCircuit(1)

p16_qc.p(math.pi / 16, 0)  # Apply a phase gate with angle pi/16 to qubit 0

p16_gate = p16_qc.to_gate(label="P(π/16)")

# Now we add two control qubits to create a controlled version of the P(π/16) gate
ctrl_p16 = p16_gate.control(2) 

print(ctrl_p16.definition.draw())