from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST

class Return(NodoAST):

    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        if isinstance(self.valor, NodoAST):
            valor =  self.valor.ejecutar(tree,table)
            return Return(valor,self.fila,self.columna)
        else:
            return self
    
    def getNodo(self):
        NodoNuevo = NodoArbol("RETURN")
        NodoNuevo.agregarHijo("return")
        if self.valor != None:
            NodoNuevo.agregarHijoNodo(self.valor.getNodo())
        NodoNuevo.agregarHijo(";")
        return NodoNuevo