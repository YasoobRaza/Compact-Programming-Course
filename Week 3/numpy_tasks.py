import numpy as np

# 1. Create a vector with values ranging from 10 to 49. Reverse a vector
v = np.arange(10, 50)
v = v[::-1]
print("Task 1:")
print(v)

# 2. Create a 5x5 array with random values and find min and max
a = np.random.random((5, 5))
print("\nTask 2:")
print("Min:", a.min())
print("Max:", a.max())

# 3. Normalize a 5x5 random matrix
a = np.random.random((5, 5))
a_norm = (a - a.min()) / (a.max() - a.min())
print("\nTask 3:")
print(a_norm)

# 4. Multiply a 5x3 matrix by a 3x2 matrix
a = np.random.random((5, 3))
b = np.random.random((3, 2))
c = a.dot(b)
print("\nTask 4:")
print(c)

# 5. Get dates of yesterday, today and tomorrow
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("\nTask 5:")
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 6. Extract integer part of a random array using 5 different methods
a = np.random.random(5) * 10
print("\nTask 6:")
print("Original:", a)
print("Method 1:", a - a % 1)
print("Method 2:", np.floor(a))
print("Method 3:", np.ceil(a) - 1)
print("Method 4:", a.astype(int))
print("Method 5:", np.trunc(a))

# 7. Create a structured array representing a position (x,y) and a color (r,g,b)
structured_array = np.zeros(10, dtype=[('position', [('x', float), ('y', float)]), 
                                       ('color', [('r', int), ('g', int), ('b', int)])])
print("\nTask 7:")
print(structured_array)

# 8. Generator function to build an array
def generator():
    for i in range(10):
        yield i
gen_array = np.fromiter(generator(), dtype=int)
print("\nTask 8:")
print(gen_array)

# 9. Check if two random array A and B are equal
A = np.random.random((3,3))
B = np.random.random((3,3))
equal = np.array_equal(A, B)
print("\nTask 9:")
print("Equal:", equal)

# 10. Random vector with shape (100,2) representing coordinates, find point by point distances
Z = np.random.random((100, 2))
distances = np.sqrt(np.sum((Z[1:] - Z[:-1])**2, axis=1))
print("\nTask 10:")
print(distances[:5])

# 11. Subtract the mean of each row of a matrix
X = np.random.random((5, 5))
Y = X - X.mean(axis=1).reshape((5, 1))
print("\nTask 11:")
print(Y)

# 12. Sort an array by the nth column
Z = np.random.random((5, 5))
n = 1
sorted_Z = Z[Z[:, n].argsort()]
print("\nTask 12:")
print(sorted_Z)

# 13. Compute a matrix rank
Z = np.random.random((3, 3))
rank = np.linalg.matrix_rank(Z)
print("\nTask 13:")
print(rank)

# 14. 16x16 array, get block-sum (block size 4x4)
Z = np.ones((16, 16))
block_size = 4
result = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        result[i, j] = Z[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size].sum()
print("\nTask 14:")
print(result)
