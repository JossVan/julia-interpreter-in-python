from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST
class Arreglos(NodoAST):

    def __init__(self, contenido, fila, columna):
        self.contenido = contenido
        self.fila = fila 
        self.columna = columna
        self.contador = 0
    
    def ejecutar(self, tree, table):
        
        for dimension in self.contenido:
            if not isinstance(dimension,list):
                break
        arreglo = self.convertir(tree,table,self.contenido,[])
        return arreglo

    def convertir(self,tree,table,item,lista):

        if isinstance(item, list):
            for i in item:
                self.convertir(tree,table,i,lista)
        elif isinstance(item, Arreglos):
            valor = item.ejecutar(tree,table)
            lista.append(valor)
        else:
            lista.append(item)
        return lista

    def aumentar(self):
        self.contador+1
        
    def getLength(self):
        return len(self.contenido)

    def getNodo(self):
        NodoPadre = NodoArbol("Arreglo")
        NodoPadre.agregarHijo("[")
        cont = 1
        for dimension in self.contenido:
            if isinstance(dimension, NodoAST):
                nodo = dimension.getNodo()
                NodoPadre.agregarHijoNodo(nodo)
                if cont< len(self.contenido):
                    NodoPadre.agregarHijo(",")
                    cont = cont+1
        NodoPadre.agregarHijo("]")
        return NodoPadre