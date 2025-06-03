
# Quantum teleportation is not about physically transporting matter. 
# Instead, it’s a way to transfer a quantum state from one qubit (Alice’s) to another (Bob’s), using entanglement and classical communication.


from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.quantum_info import Statevector

# The teleportation circuit involves three qubits:
# 	1.	q0 – Alice’s qubit holding the state |ψ⟩.
# 	2.	q1 – Alice’s half of an entangled pair.
# 	3.	q2 – Bob’s half of the entangled pair.


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_bloch_vector, plot_state_qsphere

# Quantum and classical registers
qreg = QuantumRegister(3, 'q')
creg = ClassicalRegister(2, 'c')
qc = QuantumCircuit(qreg, creg)

# STEP 0: Prepare the state |ψ⟩ on q0 (Alice's state)
qc.initialize([0.6, 0.8], 0)  # Example Alice state |ψ⟩ = 0.6|0⟩ + 0.8|1⟩


# STEP 1: Entangle q1 and q2 (EPR pair)
qc.h(1)
qc.cx(1, 2)
qc.barrier()


state = Statevector.from_instruction(qc)

plot_state_qsphere(state)

# STEP 2: Bell measurement on q0 and q1
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])  # Measure q0 → c0, q1 → c1
qc.barrier()




# STEP 3: Conditional correction on Bob's qubit q2
qc.x(2).c_if(creg, 0b10)  # if creg == 2
qc.x(2).c_if(creg, 0b11)  # if creg == 3
qc.z(2).c_if(creg, 0b01)  # if creg == 1
qc.z(2).c_if(creg, 0b11)  # if creg == 3


print(qc.draw())

# # Execute
backend = Aer.get_backend('aer_simulator_statevector')
tqc = transpile(qc, backend)
job = backend.run(tqc)
result = job.result()

