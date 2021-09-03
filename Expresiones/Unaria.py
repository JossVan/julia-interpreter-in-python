from Abstractas.NodoAST import NodoAST

class Unaria(NodoAST):

    def __init__(self, operador, fila, columna):
        self.operdador = operador
        self.fila = fila
        self.columna = columna 
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()
        