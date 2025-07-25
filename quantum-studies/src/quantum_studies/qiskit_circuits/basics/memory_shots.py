from qiskit import QuantumCircuit, transpile
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


qc = QuantumCircuit(2, 2)

qc.h([0, 1])

qc.measure([0, 1], [0, 1])

backend = BasicAer.get_backend('qasm_simulator')
job: BaseJob = execute(qc, backend, shots=10, memory=True)

result = job.result()
memory = result.get_memory(qc)
print("Memory shots:", memory)  # Print the memory shots
