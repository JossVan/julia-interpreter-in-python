from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST

class Return(NodoAST):

    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        if self.valor != None:
            self.valor = self.valor.ejecutar(tree,table)
            return self
        else:
            return self
    
    def getNodo(self):
        NodoNuevo = NodoArbol("Return")
        if self.valor != None:
            return NodoNuevo.agregarHijoNodo(self.valor.getNodo())
        return NodoNuevo