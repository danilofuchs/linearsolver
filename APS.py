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
    return(interpolado)

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
    return pontoTeste

def gaussSeidel(matrix: np.ndarray, initial: np.ndarray, maxErr10, nDigits) :
    nVariaveis = matrix.shape[0] 

    x0 = np.array(initial, float) #valor inicial
    x1 = x0.copy()
    erro = np.Infinity
    while erro > pow(10, maxErr10) : #criterio de parada
        maximaDiferenca = 0
        for n in range(nVariaveis) :
            #termo independente
            somaTemporaria = matrix[n][nVariaveis]
            
            for j in range(nVariaveis) :
                if j != n :
                    #faz uma subtracao dos outros coeficientes multiplicados por seus valores antigos
                    somaTemporaria += (- matrix[n][j])*(x1[j])
            #divide esta soma pelo proprio coeficiente
            x1[n] = somaTemporaria / matrix[n][n]
            

            diferenca = np.abs(x1[n]-x0[n])
            if diferenca > maximaDiferenca :
                maximaDiferenca = diferenca
        erro = maximaDiferenca
        x0 = x1.copy()
        if (nDigits >= 0) :
            x0 = x0.round(nDigits)

    return x0

def simpson(function, limites: tuple, numeroParticoes, casasDecimas = 6) :
    
    soma = round(function(limites[0]), casasDecimas) + round(function(limites[1]), casasDecimas)
    h = (limites[1] - limites[0]) / numeroParticoes

    for i in range (1, numeroParticoes) :
        if i % 2 == 0 :
            soma += round((2*function(limites[0] + i*h)), casasDecimas)
        else :
            soma += round((4*function(limites[0] + i*h)), casasDecimas)

    return round((h/3) * soma, casasDecimas)

def calcParticoesSimpson(function4Derivada, limites: tuple, passo) :
    return np.ceil((limites[1]-limites[0])/(2*passo))