
from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST

from Abstractas.NodoAST import NodoAST

class Break(NodoAST):

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        return self
    def getNodo(self):
        NuevoNodo = NodoArbol("BREAK")
        NuevoNodo.agregarHijo("break")
        NuevoNodo.agregarHijo(";")
        return NuevoNodo