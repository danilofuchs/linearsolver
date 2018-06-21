import numpy as np

def f(x) :
    return x**3 + x**2 + 1

def bisseccao (funcao, limites: tuple, errMax10):
    numeroIteracoes = int(np.ceil((((np.log10(limites[1] - limites[0]) - errMax10) / np.log10(2)) + 1)))

    print (numeroIteracoes)
    limites = np.array(limites, np.float)
    print (limites)

    for i in range (0, numeroIteracoes) :
        pontoTeste = np.average(limites)
        #print ('{0} {1} {2} = {3} {4} {5}'.format(limites[0], pontoTeste, limites[1], funcao(limites[0]), funcao(pontoTeste), funcao(limites[1])))
        if funcao(pontoTeste) * funcao(limites[0]) < 0 :
            limites[1] = pontoTeste
        elif funcao(pontoTeste) * funcao(limites[1]) < 0 :
            limites[0] = pontoTeste
        else :
            a = 1
            #return pontoTeste
    return pontoTeste

print (bisseccao(f, (-2, -1), -3))