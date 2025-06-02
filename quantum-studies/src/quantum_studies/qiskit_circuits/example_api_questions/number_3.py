
from qiskit import QuantumCircuit, QuantumRegister


inp_req = QuantumRegister(2, name='inp')
ancilla = QuantumRegister(1, name='ancilla')
qc = QuantumCircuit(inp_req, ancilla)

# qc.h(inp_req)
# qc.x(ancilla)
# print(qc.draw())


qc.h(inp_req[0:2]) # Selects the first two qubits in the register inp_req
qc.x(ancilla[0])
print(qc.draw())