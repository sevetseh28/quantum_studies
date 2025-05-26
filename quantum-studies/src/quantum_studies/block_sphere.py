from qutip import Bloch, basis
import matplotlib.pyplot as plt

# Define qubit states
psi = (basis(2, 0) + basis(2, 1)).unit()  # |+> state = (|0> + |1>) / sqrt(2)

# Create a Bloch sphere
b = Bloch()
b.add_states(psi)
b.render()
plt.show()