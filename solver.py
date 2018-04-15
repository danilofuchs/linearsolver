import numpy as np

def sumLines(lineA: np.ndarray, lineB: np.ndarray):
    return lineA + lineB

def multLine(line: np.ndarray, mult):
    return line.__mul__(mult)

def swapLines(matrix: np.ndarray, lineindex1, lineIndex2) :
    matrix[[lineindex1,lineIndex2]] = matrix[[lineIndex2,lineindex1]]
    return matrix

def retroDistribution(matrix: np.ndarray, nDigits) :
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
                for x in range (nVar) :
                    if x != i :
                        matrix[x] = sumLines(matrix[x], multLine(matrix[i], -matrix[x][lastCoef[1]]))
                        if nDigits >= 0 :
                            matrix = matrix.round(nDigits)

    result = np.array([0 for x in range(nVar)], np.float)
    for i in range(nVar) :
        for j in range(nVar) :
            if matrix[i][j] != 0 : #se acha um coeficiente != 0
                result[j] = matrix[i][nVar]

    return result

def gaussElimination(matrix: np.ndarray, nDigits):
    nVar = matrix.shape[0]

    for j in range(nVar - 1):
        for i in range(nVar - 1, j, -1):
            m = -matrix[i][j]/matrix[j][j]
            matrix[i][j] = 0
            for k in range(j + 1, nVar + 1):
                matrix[i][k] += m * matrix[j][k]
        if nDigits >= 0 :
            matrix = matrix.round(nDigits)

    return retroDistribution(matrix, nDigits)

def gaussEliminationPivot(matrix: np.ndarray, nDigits):
    nVar = matrix.shape[0]

    maxCoef = (0, 0)

    okLines = []

    for n in range(nVar) :

        for i in range(len(okLines)) :
             try :
                 okLines.index(i)
             except ValueError :
                 maxCoef = (i, 0)
        
        for i in range(nVar) :
            try :
                okLines.index(i)
            except ValueError :
                for j in range(nVar) :
                    if np.abs(matrix[i][j]) > np.abs(matrix[maxCoef]) :
                        maxCoef = (i, j)

        
        for i in range(nVar) :
            if i != maxCoef[0] :
                m = - matrix[i][maxCoef[1]] / matrix[maxCoef]
                matrix[i] = sumLines(matrix[i], multLine(matrix[maxCoef[0]], m))
                
                if nDigits >= 0 :
                    matrix = matrix.round(nDigits)
        okLines.append(maxCoef[0])

    return retroDistribution(matrix, nDigits)


def luDecomposition(matrix: np.ndarray, nDigits) :
    nVar = matrix.shape[0] #numero de linhas da matriz
    coefMatrix = np.delete(matrix, nVar, 1)
    bMatrix = np.array(matrix[:, nVar])

    L = np.array([[0 for x in range(nVar)] for y in range(nVar)]) # Matriz zerada
    U = np.array([[0 for x in range(nVar)] for y in range(nVar)]) # Matriz zerada

    gauss = matrix
    m = np.array([[0 for x in range(nVar)] for y in range(nVar)])
    for j in range(nVar - 1):
        for i in range(nVar - 1, j, -1):
            m[i][j] = -gauss[i][j]/gauss[j][j]
            gauss[i][j] = 0
            for k in range(j + 1, nVar + 1):
                gauss[i][k] += m[i][j] * gauss[j][k]
        if nDigits >= 0 :
            gauss = gauss.round(nDigits)
    print(gauss)
    print(m)

    for i in range (nVar) :
        for j in range (nVar) :
            if i < j :
                U[i][j] = gauss[i][j]
            elif i == j :
                U[i][j] = gauss[i][j]
                L[i][j] = 1
            else :
                L[i][j] = m[i][j]
            

    return L


def jacobi(matrix: np.ndarray, initial: np.ndarray, maxErr10, nDigits) :
    nVar = matrix.shape[0] 

    x0 = initial.copy() #valor inicial
    x1 = np.array([0 for x in range(nVar)], float)
    err = np.Infinity
    while err > pow(10, maxErr10) : #criterio de parada
        maxDiff = 0
        for n in range(nVar) :
            #termo independente
            tempSum = matrix[n][nVar] 
            
            for j in range(nVar) :
                if j != n :
                    #faz uma subtracao dos outros coeficientes multiplicados por seus valores antigos
                    tempSum += (- matrix[n][j])*(x0[j])
            #divide esta soma pelo proprio coeficiente
            x1[n] = tempSum / matrix[n][n]
            

            diff = np.abs(x1[n]-x0[n])
            if diff > maxDiff :
                maxDiff = diff
        err = maxDiff
        x0 = x1.copy()
        if (nDigits >= 0) :
            x0 = x0.round(nDigits)

    return x0

def gaussSeidel(matrix: np.ndarray, initial: np.ndarray, maxErr10, nDigits) :
    nVar = matrix.shape[0] 

    x0 = np.array(initial, float) #valor inicial
    x1 = x0.copy()
    err = np.Infinity
    while err > pow(10, maxErr10) : #criterio de parada
        maxDiff = 0
        for n in range(nVar) :
            #termo independente
            tempSum = matrix[n][nVar] 
            
            for j in range(nVar) :
                if j != n :
                    #faz uma subtracao dos outros coeficientes multiplicados por seus valores antigos
                    tempSum += (- matrix[n][j])*(x1[j])
            #divide esta soma pelo proprio coeficiente
            x1[n] = tempSum / matrix[n][n]
            

            diff = np.abs(x1[n]-x0[n])
            if diff > maxDiff :
                maxDiff = diff
        err = maxDiff
        x0 = x1.copy()
        if (nDigits >= 0) :
            x0 = x0.round(nDigits)

    return x0

matriz = np.array(
    [
    [-60, 70, -8, 9, 10],
    [10, 12, -22, 5, -44],
    [-16, 17, -18, 0, -200],
    [110, -12, 13, -265, 150]], np.float)
print(gaussEliminationPivot(matriz, 1))

matriz = np.array(
    [[3.12, -4.32,5.71,8.68,15.85],
    [37.43,17.8,-15.57,-59.67,-8.13],
    [12.16,-211.68,-25.35,42.17,-70.31],
    [12.85,-34.18,-13.44,61.54,-301.12]], np.float)
print(gaussElimination(matriz, 2))
#print(gauss(matriz, -1))

matriz = np.array(
    [[1, 0, 0, 0, -44],
    [-6, 1, 0, 0, 10],
    [11, -1.01, 1, 0, 150],
    [-1.6, 0.25, -0.16, 1, -200]], np.float)
print(retroDistribution(matriz, 2))

matriz = np.array(
    [[10, 12, -22, 5, -44],
    [0, 142, -140, 39, -254],
    [0, 0, 113.6, -29.61, 377.46],
    [0, 0, 0, 183.51, -146.51]], np.float)
print(retroDistribution(matriz, 2))
