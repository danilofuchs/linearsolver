import numpy as np

def e(x) :
    return np.e ** x

def log(x) :
    return np.log10(x)

def f4(x) :
    return np.e ** x

def simpson(function, limites: tuple, numeroParticoes) :
    
    soma = function(limites[0]) + function(limites[1])
    h = (limites[1] - limites[0]) / numeroParticoes
    #print ('h: {0}'.format(h))
    #print ('{0}: {1}'.format(0, function(limites[0])))
    for i in range (1, numeroParticoes) :
        #print ('{0}: {1}'.format(i, function(limites[0] + i*h)))
        if i % 2 == 0 :
            soma += (2*function(limites[0] + i*h))
        else :
            soma += (4*function(limites[0] + i*h))

    #print ('{0}: {1}'.format(i+1, function(limites[1])))

    return (h/3) * soma

def calcParticoesSimpson(function4Derivada, limites: tuple, errMax = 0.000001) :
    maxDerivada = np.max(np.abs([function4Derivada(limites[0]), function4Derivada(limites[1])]))
    numeroParticoes = int(np.ceil(((((limites[1] - limites[0])**5)/(2880 * errMax))*maxDerivada) ** (1/4))) * 2
    return numeroParticoes



print(simpson(e, (0, 1), 10))
print(simpson(log, (6, 10), 8))