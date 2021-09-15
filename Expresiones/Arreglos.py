from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Simbolo import Simbolo
from Abstractas.NodoAST import NodoAST

class Arreglos(NodoAST):

    def __init__(self, contenido, fila, columna):
        self.contenido = contenido
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        
        for dimension in self.contenido:
            if not isinstance(dimension,list):
                break

        return self.contenido

    def getNodo(self):
        NodoPadre = NodoArbol("Valores")

        for dimension in self.contenido:
            if isinstance(dimension, NodoAST):
                nodo = dimension.getNodo()
                NodoPadre.agregarHijoNodo(nodo)
        return NodoPadre