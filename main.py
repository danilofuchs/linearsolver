from appJar import gui
from solver import gaussElimination

    

app = gui("Linear Solver")
app.setPadding([5,5])

nMax = 4;
n = 2
res = 1
maxErr = -10

def getMatrix() :
    matrix = [[0 for x in range(n+1)] for y in range(n)] 
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

    method = app.getSpinBox('spinboxMethods')

    if method == 'Gauss' :
        result = gaussElimination(matrix,n, res)
        result = ''
        for i in range (0, n) :
            result += 'x' + str(i) + ' = ' + str(result[i]) + '\n' 
        app.infoBox("Gauss - Resultados", result);
    elif method == 'Pivoteamento Completo' :
        app.infoBox("Pivoteamento Completo", "Você clicou em Pivoteamento Completo");
    elif method == 'L.U.' :
        app.infoBox("L.U.", "Você clicou em L.U.");
    elif method == 'Jacobi' :
        app.infoBox("Jacobi", "Você clicou em Jacobi");

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
            n = int(app.getSpinBox('spinboxN'))
        else :
            n = 2
        for i in range (0, nMax) :
            for j in range (0, nMax+1) :
                title = 'a'+str(i)+str(j)
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
            res = int(app.getSpinBox('spinboxRes'))
            maxErr = int(app.getSpinBox('Erro (10^x)'))
        except :
            res = 1
        


            #app.setEntryInvalid(title)
generateMatrix()
n = 2
updateParams('firstRun')

app.startLabelFrame('Parâmetros', colspan=5)

app.addLabel('n', column=0, row=0);
app.addSpinBoxRange('spinboxN', fromVal=2,toVal=4, column=1, row=0);
app.setSpinBoxChangeFunction('spinboxN', updateParams)

app.addLabel('Método', column=0, row=3);
app.addOptionBox('spinboxMethods', ['Gauss', 'Pivoteamento Completo', 'L.U.', 'Jacobi'], column=1, row=3)
app.setOptionBoxChangeFunction('spinboxMethods', updateParams)

app.addLabel('Resolução (casas decimais)', column=0, row=1);
app.addSpinBoxRange('spinboxRes', fromVal=-1, toVal=10, column=1, row=1)
app.setSpinBoxChangeFunction('spinboxRes', updateParams)

app.addLabel('Erro (10^x)', column=0, row=2);
app.addSpinBoxRange('spinboxErr', fromVal=-10, toVal=-1, column=1, row=2)
app.setSpinBoxChangeFunction('spinboxErr', updateParams)

app.stopLabelFrame()

app.startLabelFrame('Respostas', row=4, column=5, colspan=2)

for i in range (0, nMax) :
    app.addLabel('=x' + str(i) + 'label', 'x' + str(i) + '= ', column=0, row=i);
    app.addNumericEntry('=x' + str(i), column=1, row=i)
    app.setEntry('=x' + str(i), '0')


app.stopLabelFrame()

app.setSticky('sw')
app.addButton('Solucionar', solve, row=8)

app.setSticky('se')
app.addButton("Sair", app.stop, row=8, column=8)


app.go()