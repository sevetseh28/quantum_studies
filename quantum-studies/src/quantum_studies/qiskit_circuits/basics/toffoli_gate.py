
from qiskit.circuit.library import CCXGate


toffoli_gate = CCXGate()

print(toffoli_gate.definition.draw())