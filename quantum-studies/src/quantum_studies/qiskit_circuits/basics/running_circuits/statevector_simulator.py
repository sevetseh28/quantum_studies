from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator
from qiskit_aer import AerJob
from qiskit.result import Result

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)

statevector_simulator = StatevectorSimulator()
job: AerJob = statevector_simulator.run(qc)
result: Result = job.result()
statevector = result.get_statevector(decimals=2) # Get the statevector with 4 decimal places
print("Statevector:", statevector)

# State vector is one shot - it is not probabilistic like the QASM simulator.