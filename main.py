from appJar import gui


    

app = gui("Linear Solver")
app.setPadding([5,5])

nMax = 4;
n = 2
res = 1

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

    if button == 'Gauss' :
        app.infoBox("Gauss", "Você clicou em Gauss");
    elif button == 'Pivoteamento Completo' :
        app.infoBox("Pivoteamento Completo", "Você clicou em Pivoteamento Completo");
    elif button == 'L.U.' :
        app.infoBox("L.U.", "Você clicou em L.U.");
    elif button == 'Jacobi' :
        app.infoBox("Jacobi", "Você clicou em Jacobi");

def generateMatrix() :  
    for i in range (0, nMax) :
        for j in range (0, nMax+1) :
            title = 'a'+str(i)+str(j)
            app.addNumericEntry(title, i, j)
            
            app.setEntryDefault(title, '0')
        
def updateParams() :
    try :
        n = int(app.getSpinBox('n'))
        res = int(app.getSpinBox('resolucao'))
    except :
        n = 2
        res = 1
    
    for i in range (0, nMax) :
        for j in range (0, nMax+1) :
            title = 'a'+str(i)+str(j)
            if j > n :
                app.setEntryBg(title, "grey")
            elif i >= n :
                app.setEntryBg(title, "grey")
            else :
                app.setEntryBg(title, "white")


            #app.setEntryInvalid(title)

generateMatrix()
updateParams()

app.startLabelFrame("Parâmetros", colspan=2)
app.addSpinBoxRange("n", fromVal=2,toVal=4);
app.addLabelSpinBoxRange("Resolucao", fromVal=1, toVal=10)
app.addButton("OK", updateParams)
app.stopLabelFrame()

app.startLabelFrame("Solução", colspan=2)
app.addButtons(['Gauss', 'Pivoteamento Completo', 'L.U.', 'Jacobi'], solve)
app.stopLabelFrame()


app.addButton("Sair", app.stop)

app.go()