def matmult(A,B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    if cols_A==rows_B:
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    C[i][j] += A[i][k] * B[k][j]
    return C
print(matmult([[1,2],[3,4]],[[1,0],[0,1]]))
print(matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]]))