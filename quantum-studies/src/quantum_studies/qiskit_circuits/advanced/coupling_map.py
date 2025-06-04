from qiskit import QuantumCircuit

from qiskit.providers.aer import Aer

qc = QuantumCircuit(3)


# The following 
copuling_map = [
    [0, 1], # First qubit is connected to the second
    [1, 2], # Second qubit is connected to the third
]

#   Defining the coupling map in Qiskit is useful because it encodes the physical connectivity constraints of a quantum device, 
    # specifying which pairs of qubits can directly interact via two-qubit gates like CNOT. Here’s why this is important:
	# •	Hardware Realism: Real quantum hardware cannot perform two-qubit gates between arbitrary pairs of qubits; 
        # it is limited by its physical layout. The coupling map reflects these limitations, ensuring your circuit can actually run on the device.
	# •	Efficient Compilation: When you transpile a circuit for a specific device, Qiskit uses the coupling map to adapt your circuit to the hardware.
        # If a required two-qubit operation is not directly supported, the transpiler inserts SWAP gates to move qubits into positions where the operation becomes possible.
	# •	Optimization: By knowing the connectivity, the transpiler can optimize the placement and routing of qubits, 
    # minimizing the number of SWAPs and reducing circuit depth, which improves fidelity and execution time.
	# •	Error Reduction: Fewer SWAPs and more efficient routing mean fewer gates, which reduces the chance of errors accumulating during computation.
	# •	Custom Topologies: For simulation or custom hardware, you can define your own coupling map to test algorithms under different connectivity constraints.