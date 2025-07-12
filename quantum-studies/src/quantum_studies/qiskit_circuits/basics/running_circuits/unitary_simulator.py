from qiskit import QuantumCircuit
from qiskit_aer import UnitarySimulator


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
job = UnitarySimulator().run(qc)
result = job.result()
unitary = result.get_unitary(decimals=4)  # Get the unitary matrix with 4 decimal places
print("Unitary matrix:", unitary)