from Abstractas.NodoAST import NodoAST

class If(NodoAST):

    def __init__(self, condicion, instrucciones_if, instrucciones_elseif, instrucciones_else, fila, columna):
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.instrucciones_elseif = instrucciones_elseif
        self.instrucciones_else = instrucciones_else 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return "Hola, soy el if"
    
    def getNodo(self):
        return super().getNodo()