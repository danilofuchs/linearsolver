import numpy as np

def e(x) :
    return np.e ** x

def log(x) :
    return np.log10(x)

def f4(x) :
    return np.e ** x

def ex96(x) :
    return (6*x-5)**(1/2)

def simpson(function, limites: tuple, numeroParticoes, casasDecimas = 6) :
    
    soma = round(function(limites[0]), casasDecimas) + round(function(limites[1]), casasDecimas)
    h = (limites[1] - limites[0]) / numeroParticoes
    #print ('h: {0}'.format(h))
    #print ('{0}: {1}'.format(0, function(limites[0])))
    for i in range (1, numeroParticoes) :
        #print ('{0}: {1}'.format(i, function(limites[0] + i*h)))
        if i % 2 == 0 :
            soma += round((2*function(limites[0] + i*h)), casasDecimas)
        else :
            soma += round((4*function(limites[0] + i*h)), casasDecimas)

    #print ('{0}: {1}'.format(i+1, function(limites[1])))

    return round((h/3) * soma, casasDecimas)

def calcParticoesSimpson(function4Derivada, limites: tuple, errMax = 0.000001) :
    maxDerivada = np.max(np.abs([function4Derivada(limites[0]), function4Derivada(limites[1])]))
    numeroParticoes = int(np.ceil(((((limites[1] - limites[0])**5)/(2880 * errMax))*maxDerivada) ** (1/4))) * 2
    return numeroParticoes

def trapezio(function, limites: tuple, numeroParticoes, casasDecimas = 6) :
    soma = round(function(limites[0]), casasDecimas) + round(function(limites[1]), casasDecimas)
    h = (limites[1] - limites[0]) / numeroParticoes
    #print ('h: {0}'.format(h))
    #print ('{0}: {1}'.format(0, function(limites[0])))
    for i in range (1, numeroParticoes) :
        #print ('{0}: {1}'.format(i, function(limites[0] + i*h)))
        soma += round((2*function(limites[0] + i*h)), casasDecimas)

    #print ('{0}: {1}'.format(i+1, function(limites[1])))

    return round((h/2) * soma, casasDecimas)



#print(simpson(e, (0, 1), 10))
#print(simpson(log, (6, 10), 8))
#print(trapezio(ex96, (1, 9), 8))

def moodle1(x) :
    return (3 - x**3 + np.cos(x))
print(trapezio(moodle1, (-4,-2), 8))

def moodle2(x) :
    return (3 - x**3 + np.cos(x))
print(simpson(moodle2, (-2,1), 8))

def moodle3(x) :
    return (x**2 - 4*x + 5)**(1/2)
print(simpson(moodle3, (-3,2), 10))

def moodle4(x) :
    return (6*x - 5)**(1/2)
print(simpson(moodle4, (3,11), 10))

def moodle10_2(x) :
    return (6*x - 5)**(1/2)
print(simpson(moodle10_2, (5, 13), 10))

def moodle10_3(x) :
    return (x**2 - 4*x + 5)**(1/2)
print(simpson(moodle10_3, (-4, 1), 10))