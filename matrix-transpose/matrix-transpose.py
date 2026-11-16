import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
        n=len(A)
        m=len(A[0])

        output=[[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                output[j][i]=A[i][j]
        return np.array(output)
    
