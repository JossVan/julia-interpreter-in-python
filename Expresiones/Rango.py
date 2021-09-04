from Abstractas.NodoAST import NodoAST


class Rango(NodoAST):

    def __init__(self, id, izquierdo,derecho, fila, columna):
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.id = id
        self.fila = fila
        self.columna = columna
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
