import numpy as np
from qiskit.quantum_info import SparsePauliOp


op1 = SparsePauliOp.from_sparse_list(
    [("I", 0), ("X", 1), ("Y", 2), ("Z", 3)], num_qubits=5
)