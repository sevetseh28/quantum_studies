from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h([0, 1])
qc.barrier()
qc.x(0)
qc.x(0)
qc.s(1)
qc.barrier([1])
qc.barrier(1)
qc.barrier()
qc.s(1)
print(qc.draw())  # Visualize the circuit