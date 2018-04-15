from appJar import gui
import numpy as np
from solver import gaussElimination, luDecomposition, jacobi
    
app = gui("Linear Solver")
app.setPadding([5,5])

def init() :
    global nMax
    nMax = 4;
    global n
    n = 2
    global res
    res = 1
    global maxErr
    maxErr= -10

def getParams() :
    global n
    global nMax
    global res
    global maxErr
    return {'n': n, 'nMax': nMax, 'res': res, 'maxErr': maxErr}

def setParams(**kwargs) :
    global nMax
    global n
    global res
    global maxErr
    nMaxTemp = kwargs.get('nMax', None)
    nTemp = kwargs.get('n', None)
    resTemp = kwargs.get('res', None)
    maxErrTemp = kwargs.get('maxErr', None)
    if nMaxTemp != None :
        nMax = nMaxTemp
    if nTemp != None :
        n = nTemp
    if resTemp != None :
        res = resTemp
    if maxErrTemp != None :
        maxErr = maxErrTemp
    return 0


def getMatrix() :
    n = getParams()['n']
    matrix = np.array([[0 for x in range(n+1)] for y in range(n)])
    #matrix = [[0 for x in range(n+1)] for y in range(n)] 
    for i in range (0, n) :
        for j in range (0, n+1) :
            title = 'a'+str(i)+str(j)
            try :
                matrix[i][j] = int(app.getEntry(title))
            except TypeError :
                matrix[i][j] = 0
    return matrix

def solve(button) :
    matrix = getMatrix()
    n = getParams()['n']
    res = getParams()['res']
    method = app.getOptionBox('spinboxMethods')

    if method == 'Gauss' :
        result = gaussElimination(matrix, res)
        #print(result)
        for i in range (0, n) :
            app.setEntry('resultX' + str(i), str(result[i]));
            app.setEntryBg('resultX' + str(i), 'yellow')
    elif method == 'Pivoteamento Completo' :
        app.infoBox("Pivoteamento Completo", "Você clicou em Pivoteamento Completo");
    elif method == 'L.U.' :
        result = luDecomposition(matrix, res)
        #print(result)
        for i in range (0, n) :
            app.setEntry('resultX' + str(i), str(result[i]));
            app.setEntryBg('resultX' + str(i), 'yellow')
    elif method == 'Jacobi' :
        result = jacobi(matrix, res)
        #print(result)
        for i in range (0, n) :
            app.setEntry('resultX' + str(i), str(result[i]));
            app.setEntryBg('resultX' + str(i), 'yellow')
    elif method == 'Gauss-Seidel' :
        app.infoBox("Gauss-Seidel", "Você clicou em Gauss-Seidel");

def generateMatrix() :  
    for i in range (0, nMax) :
        for j in range (0, nMax+1) :
            title = 'a'+str(i)+str(j)
            app.addLabel('x' + str(i)+str(j), 'X' + str(j) + ' +', i, 2*j+1)
            app.addNumericEntry(title, i, 2*j)
            app.setEntryDefault(title, '0')
        
def updateParams(obj) :
    if obj == 'spinboxN' or obj == 'firstRun' :
        if obj != 'firstRun' :
            setParams(n = int(app.getSpinBox('spinboxN')))
        else :
            setParams(n = 2)
        nMax = getParams()['nMax']
        for i in range (0, nMax) :
            for j in range (0, nMax+1) :
                title = 'a'+str(i)+str(j)
                n = getParams()['n']
                if j <= n and i < n :
                    #app.setLabel('x' + str(i)+str(j), 'X' + str(j) + ' +')
                    app.setEntryBg(title, "white")
                else :
                    app.setEntryBg(title, "grey")

                if i < n :
                    if j == n-1 :
                        app.setLabel('x' + str(i)+str(j), 'X' + str(j) + ' =' )
                    elif j >= n :
                        app.setLabel('x' + str(i)+str(j), '' )
                    else :
                        app.setLabel('x' + str(i)+str(j), 'X' + str(j) + ' +' )
                else :
                    app.setLabel('x' + str(i)+str(j), '' )

                    
                # else :
                #     app.setLabel('x' + str(i)+str(j), 'X' + str(j) + ' +')
                #     app.setEntryBg(title, "white")
    
    else :
        try :
            setParams(res = int(app.getSpinBox('spinboxRes')))
            setParams(maxErr = int(app.getSpinBox('Erro (10^x)')))
        except :
            setParams(res = 1)
        
    for i in range (0, getParams()['nMax']) :
        app.setEntryBg('resultX' + str(i), 'white')
        app.setEntry('resultX' + str(i),  '0')

            #app.setEntryInvalid(title)

init()
generateMatrix()


app.startLabelFrame('Parâmetros', colspan=5)

app.addLabel('n', column=0, row=0);
app.addSpinBoxRange('spinboxN', fromVal=2,toVal=4, column=1, row=0);
app.setSpinBoxChangeFunction('spinboxN', updateParams)

app.addLabel('Método', column=0, row=3);
app.addOptionBox('spinboxMethods', ['Gauss', 'Pivoteamento Completo', 'L.U.', 'Jacobi', 'Gauss-Seidel'], column=1, row=3)
app.setOptionBoxChangeFunction('spinboxMethods', updateParams)

app.addLabel('Casas decimais (-1 = todas disp.)', column=0, row=1);
app.addSpinBoxRange('spinboxRes', fromVal=-1, toVal=10, column=1, row=1)
app.setSpinBoxChangeFunction('spinboxRes', updateParams)

app.addLabel('Erro (10^x)', column=0, row=2);
app.addSpinBoxRange('spinboxErr', fromVal=-10, toVal=-1, column=1, row=2)
app.setSpinBoxChangeFunction('spinboxErr', updateParams)

app.stopLabelFrame()

app.startLabelFrame('Respostas', row=4, column=5, colspan=2)

nMax = getParams()['nMax']
for i in range (0, nMax) :
    app.addLabel('resultX' + str(i) + 'label', 'x' + str(i) + '= ', column=0, row=i);
    app.addNumericEntry('resultX' + str(i), column=1, row=i)
    app.setEntry('resultX' + str(i), '0')


app.stopLabelFrame()

app.setSticky('sw')
app.addButton('Solucionar', solve, row=8)

app.setSticky('se')
app.addButton("Sair", app.stop, row=8, column=8)

updateParams('firstRun')


app.go()