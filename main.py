from appJar import gui


    

app = gui("Linear Solver")
app.setPadding([5,5])

nMax = 4;
n = 2

def testeCallback() :
    app.infoBox("Teste", "Você clicou em teste");
    
def solve(button) :
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
        
def updateMatrix() :
    try :
        n = int(app.getSpinBox('n'))
    except :
        n = 2
    
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
updateMatrix()

app.startLabelFrame("Parâmetros", colspan=2)
app.addSpinBoxRange("n", fromVal=2,toVal=4);
app.addButton("OK", updateMatrix)
app.stopLabelFrame()

app.startLabelFrame("Solução", colspan=2)
app.addButtons(['Gauss', 'Pivoteamento Completo', 'L.U.', 'Jacobi'], solve)
app.stopLabelFrame()


app.addButton("Sair", app.stop)

app.go()