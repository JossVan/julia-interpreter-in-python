from Abstractas.NodoAST import NodoAST
from Abstractas.NodoArbol import NodoArbol
class Continue(NodoAST):

    def __init__(self, fila, columna):
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return self
    
    def getNodo(self):
        NuevoNodo = NodoArbol("CONTINUE")
        NuevoNodo.agregarHijo("continue")
        NuevoNodo.agregarHijo(";")
        return NuevoNodo
