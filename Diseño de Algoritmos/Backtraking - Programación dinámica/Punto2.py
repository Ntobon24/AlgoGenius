#Paradigma utilizado -> Programación dinamica

def MaximumPath(N, Matrix):
    matriz_sumas_maximas = [[0] * N for _ in range(N)]

    for j in range(N):
        matriz_sumas_maximas[N-1][j] = Matrix[N-1][j]
    
    for i in range(N - 2, -1, -1):
        for j in range(N):
            matriz_sumas_maximas[i][j] = Matrix[i][j] + max(matriz_sumas_maximas[i+1][j], matriz_sumas_maximas[i+1][max(0, j-1)], matriz_sumas_maximas[i+1][min(N-1, j+1)])
    
    max_sum = max(matriz_sumas_maximas[0])   
    return max_sum
Matrix = [[348, 391], [618, 193]]
N = 2
print("La suma esperada es:", MaximumPath(N, Matrix))
