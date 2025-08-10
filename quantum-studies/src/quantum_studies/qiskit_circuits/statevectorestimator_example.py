from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

# Step 1: Create a simple quantum circuit
circuit = QuantumCircuit(2)
circuit.h(0)        # Apply Hadamard gate to qubit 0
circuit.cx(0, 1)    # Apply CNOT gate (control=0, target=1)
# This creates a Bell state: |00⟩ + |11⟩

# Step 2: Define an observable (what we want to measure)
# Let's measure the Z operator on the first qubit
observable = SparsePauliOp.from_list([("ZI", 1.0)])  # Z on qubit 0, Identity on qubit 1
# When you apply the ZI observable to your Bell state, you’re asking: “What’s the average spin measurement of the first qubit along the z-axis?”

# Step 3: Create an Estimator and run the calculation
estimator = StatevectorEstimator()
job = estimator.run([(circuit, observable)])
result = job.result()

# Step 4: Get the expectation value
expectation_value = result[0].data.evs
print(f"Expectation value of Z⊗I: {expectation_value}")

#.The crucial insight is that in a Bell state like |00⟩ + |11⟩:
# 	•	The first qubit has equal probability of being measured as |0⟩ (eigenvalue +1) or |1⟩ (eigenvalue -1)
# 	•	These outcomes are perfectly correlated with the second qubit’s state
# The expectation value of 0.0 reveals that the Bell state exhibits perfect quantum superposition - there’s no classical bias toward either spin direction.
# If you measured both qubits with the ZZ observable (measuring both in the z-basis), you’d get an expectation value of +1, indicating perfect correlation - 
# whenever you measure the first qubit as |0⟩, you’re guaranteed to measure the second as |0⟩, and same for |1⟩.