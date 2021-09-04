from Abstractas.NodoAST import NodoAST

class While(NodoAST):

    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion= condicion
        self.instrucciones = instrucciones
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
