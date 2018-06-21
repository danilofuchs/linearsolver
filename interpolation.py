import numpy as np


def lagrange(pontos: np.ndarray, xInterpolado) :
    numeroPontos = pontos.shape[0]
    polinomio = np.zeros((numeroPontos,1))
    interpolado = 0
    for i in range (0, numeroPontos) :
        termo = 1
        for j in range (0, numeroPontos) :
            if j != i :
                termo *= ((xInterpolado - pontos[j][0]) / (pontos[i][0] - pontos[j][0]))
        #print(termo)
        interpolado += termo * pontos[i][1]
    return(interpolado)

def newton(pontos: np.ndarray, grau, casasDecimais, xInterpolado) :
    numeroPontos = pontos.shape[0]
    matriz = np.zeros((numeroPontos, grau + 3))
    matriz[:,0] = pontos[:,0]
    matriz[:,1] = pontos[:,1]
    #print(matriz)
    

    for j in range (2, grau + 3) :
        for i in range (0, numeroPontos + 1 - j) :
            matriz[i][j] = np.round((matriz[i+1][j-1] - matriz[i][j-1]) / (matriz[j+i-1][0] - matriz[i][0]), casasDecimais)
            #print('num = {0}, inf = {1}, sup = {2}'.format(matriz[i][j], matriz[j+i-1][0], matriz[i][0]))
            
            #print(matriz)
        
    return(matriz)

#print(lagrange(np.array([[-1, 1], [0, 3], [1, 1], [2, 1]]), 1.5))
#print(lagrange(np.array([[-1, -3], [0, -1], [1, 1]]), 1.5))
#print(newton(np.array([[-1, 1], [0, 3], [1, 1], [2, 1]]), 3, 4, 1.5))
#print(newton(np.array([[0.2, 0.16], [0.34, 0.23], [0.4, 0.27], [0.52, 0.29], [0.6, 0.32], [0.72, 0.37]]), 2, 4, 1.5))
result = newton(np.array([[1, -6], [1.5, -15], [2.1, -37], [2.4, -52], [3, -91], [3.5, -136], [4, -193], [4.2, -220], [4.8, -315], [5.3, -412]]), 4, 4, 1.5)
'''
for i in range (result.shape[0]) :
    for j in range (result.shape[1]) :
        print('{0:.4}'.format(result[i][j]), end='\t\t')
    print('')
'''
#print(lagrange(np.array([[9, 123], [12, 144], [18, 109], [20, 98], [23, 78], [26, 94], [30, 99], [34, 115]]), 18.4))
print(lagrange(np.array([[12, 144], [18, 109], [20, 98], [23, 78]]), 18.4))