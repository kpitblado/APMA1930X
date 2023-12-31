import numpy as np

# Parameters
p = 0.4
q = 0.6
N = 10

# Define the function f(x)
def f(x):
    return x**2

# Create a matrix to store the optimal stopping strategy
matrix_size = N + 1
duck_walk_matrix = np.zeros((matrix_size, matrix_size), dtype=float)

# Makes the duck walk matrix based on the parameters
for i in range(matrix_size):
    counter = i*-1
    for j in range(matrix_size):
        if (j > i):
            duck_walk_matrix[i, j] = 0
        else:
            duck_walk_matrix[i, j] = f(counter)
            counter = counter + 2

strategy_matrix = np.zeros((matrix_size, matrix_size), dtype=str)
print(duck_walk_matrix)

# Fill in the strategy matrix and compute the value of v
v = np.zeros(matrix_size)

for i in range(N, -1, -1):
    for j in range(matrix_size):
        if (i == N):
            # Bottom row as 1s
            strategy_matrix[i, j] = str(1)
        elif (j > i):
            # If outside matrix put *
            strategy_matrix[i, j] = "*"
        else:
            # Find continue value
            continue_value = (
                q * duck_walk_matrix[i+1][j]) + (p * duck_walk_matrix[i+1][j+1])
            # Update strategy matrix accordingly
            best_value = max(duck_walk_matrix[i][j], continue_value)
            if best_value == duck_walk_matrix[i][j]:
                strategy_matrix[i][j] = str(1)
            else:
                strategy_matrix[i][j] = str(0)

            duck_walk_matrix[i][j] = best_value


# Output the value of v
print("The value of v is:", duck_walk_matrix[0][0])

# Output the optimal stopping strategy matrix
print("Optimal stopping strategy:")
for n in range(matrix_size):
    print("n =", n, strategy_matrix[n])

"""
OUTPUT TO TERMINAL:

The value of v is: 13.740240486399998
Optimal stopping strategy:
n = 0 ['0' '*' '*' '*' '*' '*' '*' '*' '*' '*' '*']
n = 1 ['0' '0' '*' '*' '*' '*' '*' '*' '*' '*' '*']
n = 2 ['0' '0' '0' '*' '*' '*' '*' '*' '*' '*' '*']
n = 3 ['0' '0' '0' '0' '*' '*' '*' '*' '*' '*' '*']
n = 4 ['0' '0' '0' '0' '1' '*' '*' '*' '*' '*' '*']
n = 5 ['0' '0' '0' '0' '0' '1' '*' '*' '*' '*' '*']
n = 6 ['0' '0' '0' '0' '0' '1' '1' '*' '*' '*' '*']
n = 7 ['0' '0' '0' '0' '0' '0' '1' '1' '*' '*' '*']
n = 8 ['0' '0' '0' '0' '0' '0' '1' '1' '1' '*' '*']
n = 9 ['0' '0' '0' '0' '0' '0' '1' '1' '1' '1' '*']
n = 10 ['1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1'

"""
