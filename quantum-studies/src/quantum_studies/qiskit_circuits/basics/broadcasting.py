import numpy as np
# https://numpy.org/doc/stable/user/basics.broadcasting.html
a = np.array([1, 2])      # shape (2,)
b = np.array([[10], [20]]) # shape (2, 1)

print(a.shape)  # (2,)
print(b.shape)  # (2, 1)

# Shapes from right to left:
# (a) ... 2 vs 1 → compatible (1 can stretch)
# (b)  — vs 2   → compatible (missing dims treated as 1)

result = a + b  # works
print(result)