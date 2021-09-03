from Abstractas.NodoAST import NodoAST

class Relacional(NodoAST):

    def __init__(self, operador1, operador2, tipooperacion, fila, columna):
        self.operador1=operador1,
        self.operador2 = operador2
        self.tipooperacion = tipooperacion
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()
    