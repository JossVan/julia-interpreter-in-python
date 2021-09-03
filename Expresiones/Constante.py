from Abstractas.NodoAST import NodoAST

class Constante(NodoAST):

    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()