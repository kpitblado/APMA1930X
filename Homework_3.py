import numpy as np
from math import comb

# Parameters
p = 0.4
N = 10

# Define the function f(x)
def f(x):
    return x**2

# Create a matrix to store the optimal stopping strategy
matrix_size = N + 1
duck_walk_matrix = np.zeros((matrix_size, matrix_size), dtype=int)

#Makes the duck walk matrix based on the parameters
for i in range(matrix_size):
    counter = i*-1
    for j in range(matrix_size):
        if(j > i):
            duck_walk_matrix[i,j] = 0
        else:
            duck_walk_matrix[i,j] = f(counter)
            counter = counter + 2        

strategy_matrix = np.zeros((matrix_size, matrix_size), dtype=str)


# Fill in the strategy matrix and compute the value of v
v = np.zeros(matrix_size)


for i in range(N , -1, -1):
    for j in range(matrix_size):
        if(i == N):
            strategy_matrix[i,j] = str(1)
        elif(j > i):
            strategy_matrix[i,j] = "*"
        else:     
            # Calculate the expected value of f(S_tau) if we stop at time n and state S_n
            stop_value = duck_walk_matrix[i,j]
            # Calculate the expected value of f(S_tau) if we continue at time n and state S_n
            continue_value = (1-p) * duck_walk_matrix[i+1,j] + p * duck_walk_matrix[i+1,j+1]
            
            if stop_value >= continue_value:
                strategy_matrix[i,j] = str(1)  # Stop
            else:
                strategy_matrix[i,j] = str(0)  # Continue
                        
       
for i in range(matrix_size):
    for j in range(matrix_size):
        if(i>=j):
            v[i] = v[i] + (duck_walk_matrix[i,j] * (1-p)**(i-j) * (p)**(j) * comb(i,j))


# Output the value of v
print("The value of v is:", max(v))

# Output the optimal stopping strategy matrix
print("Optimal stopping strategy:")
for n in range(matrix_size):
    print("n =", n, strategy_matrix[n])

# Note: The matrix contains values 1 for stop and 0 for continue.