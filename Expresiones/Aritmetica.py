from Abstractas.NodoAST import NodoAST

class Aritmetica(NodoAST):

    def __init__(self, operador1,operacion,operador2, linea,columna):
        self.operador1 = operador1
        self.operador2 = operador2
        self.operacion = operacion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()