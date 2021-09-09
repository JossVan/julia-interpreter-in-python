from Abstractas.NodoAST import NodoAST

class For(NodoAST):

    def __init__(self, id, rango, instrucciones, fila, columna):
        self.id = id
        self.rango = rango
        self.instrucciones = instrucciones
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)