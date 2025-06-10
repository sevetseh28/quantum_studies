from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.quantum_info import DensityMatrix


matrix_1 = [
    [1, 0], 
    [0, 0]
]

matrix_2 = [
    [0, 0], 
    [0, 1]
    ]



matrix_1 = DensityMatrix(matrix_1)
matrix_2 = DensityMatrix(matrix_2)

tensored_matrix = matrix_1.tensor(matrix_2)

print("Tensored Density Matrix:")
print(tensored_matrix)