from graphviz import Graph

class Arbolito:
    
    def __init__(self, instrucciones ):
        self.instrucciones = instrucciones
        self.funciones = []
        self.errores = []
        self.consola = ""
        self.TSglobal = None
        self.dot = ""
        self.contador = 0
        self.chart_data = Graph()

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getErrores(self):
        return self.errores

    def setErrores(self, errores):
        self.errores = errores

    def insertError(self, error):
        self.errores.append(error)
    
    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self,cadena):
        self.consola += str(cadena)

    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal

    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None
    
    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def getDot(self, raiz):
        #self.dot = ""
        #self.dot += "digraph {\n"
        #self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.chart_data.node("n0",raiz.getValor().replace("\"","\\\""))
        self.contador = 2
        self.recorrerAST("n0", raiz)
        chart_output = self.chart_data.pipe(format='svg').decode('utf-8')
        #self.dot += "}"
        return chart_output

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            if hijo.getValor() == "":
                hijito = "Vacío"
            else:
                hijito = hijo.getValor().replace("\"", "\\\"")
            self.chart_data.node(nombreHijo,hijito)
            self.chart_data.edge(idPadre, nombreHijo)
            #self.dot += nombreHijo + "[label=\"" + hijito + "\"];\n"
            #self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)