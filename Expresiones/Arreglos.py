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
        return super().getNodo()