import numpy as np
rng = np.random.default_rng(42)
A = np.array(rng.integers(low=0, high=10, size=(3,3)))
B = np.array(rng.integers(low=0, high=10, size=(3,3)))
ADD = A + B
SUB = A - B
MUL = A @ B
TRANSPOSE = A.T
print("A")
print(A)
print("B")
print(B)
print("ADD")
print(ADD)
print("SUB")
print(SUB)
print("MUL")
print(MUL)
print("TRANSPOSE")
print(TRANSPOSE)