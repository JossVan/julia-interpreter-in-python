from Abstractas.NodoAST import NodoAST

class Identificador(NodoAST):

    def __init__(self, id, fila, columna):
        self.id = id 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()
        