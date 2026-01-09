import numpy as np

# Task 1
# Using the NumPy functions you learned about on the previous page, create a 4 x 4 ndarray that only contains consecutive even numbers from 2 to 32 (inclusive).

X1 = np.linspace(2, 32, 16).reshape((4,4))
# print(X)


# Task 2
# Create a 5 x 5 ndarray X with consecutive integers from 1 to 25 (inclusive). Afterwards use Boolean indexing to pick out only the odd numbers in the array and assign the result to Y.

X2 = np.arange(1,26).reshape(5,5)
# print(X2)
Y2 = X2[X2%2==1]
# print(Y2)


# Task 3
# Use Broadcasting to create a 4 x 4 ndarray that has its first column full of 1s, its second column full of 2s, its third column full of 3s, etc..

# arr = np.ones(16).reshape(4,4)
# add_arr = np.array([-1, 0, 1, 2]).reshape(4,1)
X3 = np.multiply( np.ones((4,4), dtype=int), np.arange(1,5) )
# print(X3)