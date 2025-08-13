import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli
from qiskit.primitives import StatevectorEstimator

# Step 1: Create a simple quantum circuit
circuit = QuantumCircuit(1)
circuit.reset(0)
circuit.ry(np.pi/2, 0)  # Apply a rotation around the Y-axis to qubit 0 
# The above is the same as a Hadamard gate 


z_basis_obs = Pauli("Z") # To get probabilities in the Z basis

result = StatevectorEstimator().run([(circuit, z_basis_obs)]).result()


pub_result = result[0].data.evs
print(f"Expectation value of Z: {pub_result}")
print(" Standard deviation of Z: ", result[0].data.stds)

# The expectation value here is 0.0, indicating that the qubit is in a superposition state.

# Let's rotate it along the Y axis an eighth turn

circuit.ry(np.pi/4, 0)  # Apply a rotation around the Y-axis to qubit 0
result = StatevectorEstimator().run([(circuit, z_basis_obs)]).result()
pub_result = result[0].data.evs
print(f"Expectation value of Z after Ry eigth rotation: {pub_result}")
print(" Standard deviations: ", result[0].data.stds)

# The expectation value here is -0.707 = 1/np.sqrt(2),
# indicating that the qubit is now in a state where it has a higher probability of being measured as |1⟩ than |0⟩.
