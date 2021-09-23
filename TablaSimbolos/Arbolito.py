from TablaSimbolos.Errores import Errores
from TablaSimbolos.Tipos import Tipo_Acceso
from TablaSimbolos.Simbolo import Simbolo
#from graphviz import Graph
from Instrucciones.Funciones import Funciones
from datetime import datetime
class Arbolito:
    
    def __init__(self, instrucciones ):
        self.instrucciones = instrucciones
        self.funciones = []
        self.errores = []
        self.structs = []
        self.consola = ""
        self.TSglobal = None
        self.dot = ""
        self.general = []
        self.contador = 0
        #self.chart_data = Graph()
        self.cont = 0 

    def agregarTS(self, id, simbolo):

        for i in self.general:
            if isinstance(i,Simbolo):
                if i.identificador== simbolo.identificador:
                    return i
        self.general.append(simbolo)
    

    def aumentar(self):
        self.cont = self.cont+1
    
    def getCont(self):
        return self.cont
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

    def getStruct(self, nombre):
        for struct in self.structs:
            if struct.nombre == nombre:
                return struct
        return None

    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def addStruct(self, struct):
        self.structs.append(struct)

    def getDot(self, raiz):
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        #self.chart_data.node("n0",raiz.getValor().replace("\"","\\\""))
        self.contador = 1
        self.recorrerAST("n0", raiz)
        #chart_output = self.chart_data.pipe(format='svg').decode('utf-8')
        #chart_output = self.chart_data.pipe(format='png')
        #chart_output = base64.b64encode(chart_output).decode('utf-8')
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            if hijo.getValor() == "":
                hijito = "Vacío"
            else:
                hijito = hijo.getValor().replace("\"", "\\\"")
            #self.chart_data.node(nombreHijo,hijito)
            #self.chart_data.edge(idPadre, nombreHijo)
            self.dot += nombreHijo + "[label=\"" + hijito + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)
    
    def htmlTablaSimbolos(self):

        cadena = "<table class=\"table\">\n"
        cadena += "<thead>"
        cadena +="<tr>"
        cadena +="<th scope=\"col\">Nombre</th>"
        cadena +="<th scope=\"col\">Tipo</th>"
        cadena +="<th scope=\"col\">Ámbito</th>"
        cadena +="<th scope=\"col\">Fila</th>"
        cadena +="<th scope=\"col\">Columna</th>"
        cadena +="</tr>"
        cadena +="</thead>"
        cadena +="<tbody>"
        
        for simbolo in self.general:
            if isinstance(simbolo,Simbolo):
                cadena+="<tr>"
                cadena+="<td>"
                cadena+= simbolo.getID()
                cadena+="</td>"
                cadena+="<td>"
                cadena+= simbolo.getTipo()
                cadena+="</td>"
                cadena+="<td>"
                if simbolo.getAmbito() == Tipo_Acceso.GLOBAL:
                    cadena+= "Global"
                elif simbolo.getAmbito() == Tipo_Acceso.LOCAL:
                    cadena+="Local"
                elif simbolo.getAmbito() == Tipo_Acceso.NONE:
                    cadena+= "Global"
                else:
                    cadena+= simbolo.getAmbito()
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(simbolo.getFila())
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(simbolo.getColumna())
                cadena+="</td>"
                cadena+="</tr>"


        for funcion in self.getFunciones():
            if isinstance(funcion, Funciones):
                cadena+="<tr>"
                cadena+="<td>"
                cadena+= funcion.nombre
                cadena+="</td>"
                cadena+="<td>"
                cadena+= "Función"
                cadena+="</td>"
                cadena+="<td>"
                cadena+= "Global"
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(funcion.fila)
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(funcion.columna)
                cadena+="</td>"
                cadena+="</tr>"
        



        cadena+="</tbody>"
        cadena+="</table>"
        return cadena


    def htmlErrores(self):
        now = datetime.now()
        cadena = "<table class=\"table\">\n"
        cadena += "<thead>"
        cadena +="<tr>"
        cadena +="<th scope=\"col\">Error</th>"
        cadena +="<th scope=\"col\">Tipo</th>"
        cadena +="<th scope=\"col\">Descripción</th>"
        cadena +="<th scope=\"col\">Fila</th>"
        cadena +="<th scope=\"col\">Columna</th>"
        cadena +="<th scope=\"col\">Fecha y hora</th>"
        cadena +="</tr>"
        cadena +="</thead>"
        cadena +="<tbody>"
        
        for err in self.getErrores():
            if isinstance(err,Errores):
                cadena+="<tr>"
                cadena+="<td>"
                cadena+= str(err.error)
                cadena+="</td>"
                cadena+="<td>"
                print(err.tipo)
                cadena+= err.tipo
                cadena+="</td>"
                cadena+="<td>"        
                cadena+= err.descripcion
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(err.fila)
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(err.columna)
                cadena+="</td>"
                cadena+="<td>"
                cadena+= str(now.day)+"-"+str(now.month)+"-"+ str(now.year)+", "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)
                cadena+="</td>"
                cadena+="</tr>"


        cadena+="</tbody>"
        cadena+="</table>"
        return cadena