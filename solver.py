import numpy as np

def sumLines(lineA: np.ndarray, lineB: np.ndarray):
    return lineA + lineB

def multLine(line: np.ndarray, mult):
    return line.__mul__(mult)

def swapLines(matrix: np.ndarray, lineindex1, lineIndex2) :
    matrix[[lineindex1,lineIndex2]] = matrix[[lineIndex2,lineindex1]]
    return matrix

def retroDistribution(matrix: np.ndarray) :
    nVar = matrix.shape[0]
    for n in range(nVar) :
        for i in range(nVar) : #para cada linha
            numCoefsLine = 0
            lastCoef = (-1,-1)
            for j in range(nVar) : #para cada item da linha
                if matrix[i][j] != 0 : #se acha um coeficiente != 0
                    numCoefsLine += 1
                    lastCoef = (i,j)
            if numCoefsLine == 1 : #se só tem 1 coeficiente na linha
                matrix[i] = multLine(matrix[i], (1/matrix[lastCoef]))
                print(matrix)
                for x in range (nVar) :
                    if x != i :
                        matrix[x] = sumLines(matrix[x], multLine(matrix[i], -matrix[x][lastCoef[1]]))
                        print(matrix)

    result = np.array([0 for x in range(nVar)], np.float)
    for i in range(nVar) :
        for j in range(nVar) :
            if matrix[i][j] != 0 : #se acha um coeficiente != 0
                result[j] = matrix[i][nVar]

    return result

def gaussElimination(matrix: np.ndarray, nDigits):
    #results = 1
    #matrix = np.array(matrix)
    nVar = matrix.shape[0] #numero de linhas da matriz
    for j in range((nVar - 1), 0, -1): #das colunas (nVar-1) ate 0
        for i in range(nVar): #das linhas 0 ate nVar
            mult = matrix[i][j] / matrix[j][j] # mult = matriz[nvar-1][]/matriz
            matrix[i] = multLine(matrix[i], mult);
            if (nDigits >= 0) :
                matrix.round(nDigits)
            print(matrix)
    return retroDistribution(matrix)

def luDecomposition(matrix: np.ndarray, nDigits) :
    nVar = matrix.shape[0] #numero de linhas da matriz
    coefMatrix = np.delete(matrix, nVar, 1)
    bMatrix = np.array(matrix[:, nVar])

    

    print(coefMatrix)
    print(bMatrix)

    X = np.array()
    Y = np.array()

    return X