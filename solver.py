def sumLines(lineA, lineB, nTerms, nDigits):
    for i in range(nTerms):
        lineA[i] += lineB[i]
        round(lineA[i], nDigits)
    return lineA

def multLine(line, mult, nTerms, nDigits):
    for i in range(nTerms):
        line[i] *= mult
        round(line[i], nDigits)
    return line

def gaussElimination(matrix, nVar, nDigits):
    results = 1
    for j in range((nVar - 1), 0, -1): #das colunas (nVar-1) ate 0
        for i in range(nVar): #das linhas 0 ate nVar
            mult = matrix[i][j] / matrix[j][j] # mult = matriz[nvar-1][]/matriz
            multLine(matrix[i], mult, len(matrix[i]), nDigits);
    return(results)