from Abstractas.NodoAST import NodoAST

class Elemento(NodoAST):

    def __init__(self, id, tipo, fila, columna):
        self.id = id
        self.tipo = tipo
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)