from Abstractas.NodoAST import NodoAST

class Arreglos(NodoAST):

    def __init__(self,id, dim1,dim2, fila, columna):
        self.id = id
        self.dim1 = dim1
        self.dim2 = dim2
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)