from solver import gaussEliminationPivot
import numpy as np
import matplotlib.pyplot as plt


def leastSquares(xyarray: np.ndarray, pow, nDigits, plot=False) :

    
    pow = pow + 1

    numPoints = xyarray.shape[1]
    g = np.zeros((pow, numPoints))

    for i in range (0, pow) :
        for j in range (0, numPoints) :
            g[i][j] = xyarray[0][j] ** i


    matrix = np.zeros((pow, pow + 1))
    for i in range (0, pow) :
        for j in range (0, pow) :
            matrix[i][j] = np.dot(g[i], g[j])
        matrix[i][pow] = np.dot(g[i], xyarray[1])

    coeficients = gaussEliminationPivot(matrix, nDigits)

    if (plot):
        plotLeastSquares(xyarray, coeficients)  

    result = ''
    for i in range (0, pow) :
        result += '{0} * x^{1}'.format(coeficients[i], i)
        if (i < pow-1) :
            result += ' + '

    return(result)

def plotLeastSquares(points: np.ndarray, coeficients: np.ndarray) :
    min = np.min(points[0])
    min = min - 0.1 * np.abs(min)
    max = np.max(points[0])
    max = max + 0.1 * np.abs(max)

    t = np.arange(min, max, 0.01)
    s = np.zeros(t.shape)

    pow = coeficients.shape[0]
    for (i, tValue) in np.ndenumerate(t):
        for j in range (0, pow) :
            s[i] += coeficients[j] * (tValue ** j)
    plt.plot(t, s, color='C2', label='Ajuste')
    plt.scatter(x=points[0], y=points[1], color='C1', label='Pontos')
    
    plt.show()

        
leastSquares(np.array([
    [1, 2, 3],
    [3, 5, 7]
]), 1, 10, plot=False)

leastSquares(np.array([
    [1.3, 3.4, 5.1, 6.8, 8],
    [2, 5.2, 3.8, 6.1, 5.8]
]), 1, 2, plot=False)

leastSquares(np.array([
    [-1, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1],
    [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]
]), 2, 4, plot=False)

leastSquares(np.array([
    [-1.5, -1.4, -1, -0.8, -0.3, 0, 0.2, 0.6, 0.9, 1.2, 1.5],
    [-16.027, -11.12, 0.368, 2.811, 4.708, 5, 5.215, 5.304, 3.835, -0.974, -11.768]
]), 2, 5, plot=False)


leastSquares(np.array([
    [-6,-5,-4,-3,-2,-1,0,1,2],
    [-2.30258509, -1.60943791, -1.2039728,  -0.91629073, -0.51082562,  0,  0.26236426,  1.09861229,  2.07944154]
]), 1, 5, plot=False)

leastSquares(np.array([
    [-6,-5,-4,-3,-2,-1,0,1,2],
    [-2.30258509, -1.60943791, -1.2039728,  -0.91629073, -0.51082562, -0.10536052, 0.09531018,  1.09861229,  2.07944154]
]), 1, 5, plot=False)

y = np.array([0.1,0.2,0.3,0.4,0.6,0.9,1.1,3,8])
#print(np.log(y))

#print(np.e**0.59371)

leastSquares(np.array([
    [-1.1, -0.7, -0.6, -0.4, -0.2, 0, 0.3, 0.4, 0.5, 0.8, 1.1],
    [2.1, 1.2, 0.5, 0.32, 0.45, 0., 0.1, 0.5, 0.55, 1.4, 2.1]
]), 2, 5, plot=False)

print(leastSquares(np.array([
    [4, 36, 68, 100, 132, 164, 196, 218],
    [5.97177191, 5.08388576, 4.18205014, 3.28840189, 2.38876279, 1.51732262, 0.62057649, 0]
]), 1, 5, plot=True))

y = np.array([392.2, 161.4, 65.5, 26.8, 10.9, 4.56, 1.86, 1])
#print(np.log(y))
print(np.e ** 6.08176)