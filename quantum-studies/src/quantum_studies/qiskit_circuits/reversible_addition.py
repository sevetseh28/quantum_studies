from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def reversible_2bit_adder():
    # Qubit layout:
    # 0: a0 (least significant bit of A)
    # 1: a1 (most significant bit of A)
    # 2: b0 (least significant bit of B)
    # 3: b1 (most significant bit of B)
    # 4: c0 (initial carry-in, set to 0)
    # 5: c1 (carry between bits)
    # 6: c2 (final carry-out)
    # 7: s0 (sum0)
    # 8: s1 (sum1)
    # Classical bits: 3 (s1, s0, c2)
    qc = QuantumCircuit(9, 3)

    # Example input: A=10, B=01 (A=2, B=1)
    qc.x(1)  # a1 = 1 (A=10)
    qc.x(2)  # b0 = 1 (B=01)

    # Initial carry is zero (c0)
    # All ancillas (c1, c2, s0, s1) start at 0

    # --- First full adder (LSB) ---
    # Inputs: a0 (q0), b0 (q2), c0 (q4)
    # Outputs: s0 (q7), c1 (q5)
    # Sum: s0 = a0 ^ b0 ^ c0
    qc.cx(0, 7)
    qc.cx(2, 7)
    qc.cx(4, 7)
    # Carry: c1 = majority(a0, b0, c0)
    qc.ccx(0, 2, 5)
    qc.ccx(0, 4, 5)
    qc.ccx(2, 4, 5)

    # --- Second full adder (MSB) ---
    # Inputs: a1 (q1), b1 (q3), c1 (q5)
    # Outputs: s1 (q8), c2 (q6)
    qc.cx(1, 8)
    qc.cx(3, 8)
    qc.cx(5, 8)
    qc.ccx(1, 3, 6)
    qc.ccx(1, 5, 6)
    qc.ccx(3, 5, 6)

    # Measure sum and final carry
    qc.measure(8, 2)  # s1 -> cbit 2
    qc.measure(7, 1)  # s0 -> cbit 1
    qc.measure(6, 0)  # c2 -> cbit 0

    return qc

qc = reversible_2bit_adder()
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1).result()
counts = result.get_counts()
print("Result (classical bits [c2 s0 s1]):", counts)
