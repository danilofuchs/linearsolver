import numpy as np

def sumLines(lineA: np.ndarray, lineB: np.ndarray):
    return lineA + lineB

def multLine(line: np.ndarray, mult):
    return line.__mul__(mult)

def gaussElimination(matrix: np.ndarray, nDigits):
    #results = 1
    #matrix = np.array(matrix)
    nVar = matrix.shape[0]
    for j in range((nVar - 1), 0, -1): #das colunas (nVar-1) ate 0
        for i in range(nVar): #das linhas 0 ate nVar
            mult = matrix[i][j] / matrix[j][j] # mult = matriz[nvar-1][]/matriz
            matrix[i] = multLine(matrix[i], mult);
            if (nDigits >= 0) :
                matrix.round(nDigits)
            print(matrix)
    return [row[nVar] for row in matrix]