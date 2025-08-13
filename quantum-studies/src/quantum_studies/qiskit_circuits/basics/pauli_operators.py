import numpy as np
from qiskit.quantum_info import Pauli
from qiskit import QuantumCircuit


p = Pauli('IZ') # IZ pauli operator represents an Operator on a 2-qubit 
print("Pauli operator:\n", p.to_matrix())

qc = QuantumCircuit(2)
qc.unitary(p.to_matrix(), [0, 1], label='IZ From Pauli')  # Apply the Pauli operator to the circuit

qc.pauli("IZ", [0, 1])  # Apply the Pauli operator to the circuit

print(qc.draw())


# Now let's use Pauli other form of initialization - Symplectic form
z = np.array([1,1,0], dtype=bool)
x = np.array([1,0,1], dtype=bool)
# From `(z,x)`:
	# •	Qubit 0: `z=0, x=1` → X
	# •	Qubit 1: `z=1, x=0` → Z
	# •	Qubit 2: `z=1, x=1` → Y (and Y introduces a built‑in `+i` factor)
phase = 0 # Corresponds to +i

p2 = Pauli((z, x, phase))  # Create a Pauli operator with the specified z, x, and phase
p2_matrix = p2.to_matrix()  # Convert to matrix representation
label = p2.to_label()
print("Symplectic form label:", label)
print("Symplectic form matrix shape:", p2_matrix.shape)
print("Pauli operator with custom z,x,phase initialization:\n", p2_matrix)

# Build the same operator from the generated label to verify they match
label_op_matrix = Pauli(label).to_matrix()  # Use the actual generated label, not hardcoded
print("Pauli operator with label initialization", label + ":\n", label_op_matrix)

# Check if they're equal
print("Are symplectic and label matrices equal?", np.allclose(p2_matrix, label_op_matrix))
