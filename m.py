
# Matrix Multiplication

# Matrix A
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matrix B
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Result matrix initialization
result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

# Matrix multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

# Display result
print("Result Matrix:")
for row in result:
    print(row)
