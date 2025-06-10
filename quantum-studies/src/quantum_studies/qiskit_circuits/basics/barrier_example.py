from qiskit import QuantumCircuit

qc = QuantumCircuit(5)
qc.h([0, 1])
qc.barrier()
qc.x(0)
qc.x(0)
qc.s(1)
qc.barrier([1], [4, 3])
qc.barrier(0, 1)
qc.barrier()
qc.barrier(-1)
qc.barrier([-1, -2])
qc.s(1)
print(qc.draw())  # Visualize the circuit