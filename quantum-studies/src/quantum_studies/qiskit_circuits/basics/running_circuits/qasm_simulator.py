
from qiskit import QuantumCircuit
from qiskit_aer import QasmSimulator

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)
qc.measure_all()

qasm_simulator = QasmSimulator()

job = qasm_simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print("Measurement results:", counts)