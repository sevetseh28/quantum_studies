
from qiskit import QuantumCircuit, BasicAer, transpile


qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)
qc.measure_all()

backend: BasicAer = BasicAer.get_backend('qasm_simulator')
tqc = transpile(qc, backend)
job = backend.run(tqc, shots=1000)
result = job.result()
counts = result.get_counts(tqc)
print("Measurement results:", counts)