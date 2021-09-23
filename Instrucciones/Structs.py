from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST
from TablaSimbolos.Simbolo import Simbolo
class Struct(NodoAST):

    def __init__(self,mutable,nombre, elementos, fila, columna):
        self.mutable = mutable
        self.nombre = nombre
        self.elementos = elementos 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        
        return self.elementos
    
    def mutables(self):
        return self.mutable

    def getNodo(self):
        NodoNuevo = NodoArbol("STRUCT")

        if self.mutable:
            NodoNuevo.agregarHijo("MUTABLE")
        else: 
            NodoNuevo.agregarHijo("INMUTABLE")
        
        NodoElementos = NodoArbol("ELEMENTOS")
        if self.elementos != None:
            for elemento in self.elementos:
                NodoElementos.agregarHijoNodo(elemento.getNodo())
        
        NodoNuevo.agregarHijoNodo(NodoElementos)
        return NodoNuevo