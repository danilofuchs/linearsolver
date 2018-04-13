def sumLines(lineA, lineB, nTerms, nDigits):
    for i in range nTerms:
        lineA[i] += lineB[i]
        round(lineA[i], nDigits)
    return lineA

def multLine(line, m, nTerms, nDigits):
    for i in range nTerms:
        line[i] *= m
        round(line[i], nDigits)
    return line

def gaussElimination(matrix, nVar, nDigits):
    
    return(results)