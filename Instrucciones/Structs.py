from Abstractas.NodoAST import NodoAST

class Struct(NodoAST):

    def __init__(self,mutable,id, elementos, fila, columna):
        self.mutable = mutable
        self.id = id 
        self.elementos = elementos 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)