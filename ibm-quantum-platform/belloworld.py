# Qiskit code for the first circuit created, named Bello World, for its use of a Bell state
# and a play on words for the overused Hello World running gag. In this folder are also
# the corresponding files for a view of the composer, and my notes that relate to this specifically.
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
