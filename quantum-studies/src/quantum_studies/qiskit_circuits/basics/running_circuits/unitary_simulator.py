from qiskit import QuantumCircuit, BasicAer, transpile


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
backend = BasicAer.get_backend('unitary_simulator')
tqc = transpile(qc, backend)
job = backend.run(tqc)
result = job.result()
unitary = result.get_unitary(tqc, decimals=4)  # Get the unitary matrix with 4 decimal places
print("Unitary matrix:", unitary)