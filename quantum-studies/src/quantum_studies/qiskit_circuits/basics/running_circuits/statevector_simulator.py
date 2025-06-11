from qiskit import QuantumCircuit, BasicAer, transpile


qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)

backend: BasicAer = BasicAer.get_backend('statevector_simulator')
tqc = transpile(qc, backend)
job = backend.run(tqc)
result = job.result()
statevector = result.get_statevector(tqc, 8) # Get the statevector with 4 decimal places
print("Statevector:", statevector)

# State vector is one shot - it is not probabilistic like the QASM simulator.