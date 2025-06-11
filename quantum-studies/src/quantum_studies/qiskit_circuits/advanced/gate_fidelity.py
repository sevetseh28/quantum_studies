from qiskit.quantum_info import average_gate_fidelity, state_fidelity, process_fidelity, average_gate_fidelity
from qiskit.quantum_info import Operator
from qiskit.circuit.library import XGate
import numpy
# In Qiskit, gate fidelity is a measure of how accurately a quantum gate implemented on real hardware matches the ideal, 
# theoretical version of that gate. It quantifies the “closeness” between the actual operation performed by the device and the perfect gate you intended to apply.
# What Does Gate Fidelity Mean?

# •	Gate fidelity is a number between 0 and 1.
# •	1 means the actual gate is identical to the ideal gate (perfect fidelity).
# •	0 means the actual operation is completely different from the ideal.
# •	It is calculated by comparing the output of the real (noisy) gate to the output of the ideal gate, either for a specific 
# quantum state or averaged over all possible input state

x_gate = Operator(XGate())
operator_b = numpy.exp(1j * 1/2) * Operator(XGate())


# Calculate the X-gate fidelity compared to Op B
fidelity = average_gate_fidelity(channel=x_gate, target=operator_b) 
print("X-Gate Fidelity differing to X-Gate by Global Phase:", fidelity)

# Create a noisy channel 
noisy_channel = Operator(XGate().to_matrix() * 0.9 + numpy.eye(2) * 0.1)
fidelity_noisy = average_gate_fidelity(channel=noisy_channel, target=x_gate)
print("Fidelity of Noisy Channel compared to Ideal X-Gate:", fidelity_noisy)