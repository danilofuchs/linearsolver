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
        interpolado += termo * pontos[i][1]
    print(interpolado)

lagrange(np.array([[-1, 1], [0, 3], [1, 1], [2, 1]]), 1.5)
lagrange(np.array([[-1, -3], [0, -1], [1, 1]]), 1.5)