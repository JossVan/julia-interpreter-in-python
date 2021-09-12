from TablaSimbolos.Errores import Errores
from Abstractas.NodoAST import NodoAST


class Rango(NodoAST):

    def __init__(self, id, izquierdo,derecho, fila, columna):
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.id = id
        self.fila = fila
        self.columna = columna
    def ejecutar(self, tree, table):
        
        if self.id == None:
            if self.derecho == None:
                izquierdo =""
                try:
                    izquierdo = self.izquierdo.ejecutar(tree,table)
                    return izquierdo
                except:
                    err= Errores(izquierdo,"Semántico", "Error en el rango", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.derecho != None and self.izquierdo != None:
                try:
                    izquierdo = self.izquierdo.ejecutar(tree,table)
                    derecho = self.derecho.ejecutar(tree,table)
                    if isinstance(izquierdo,int) and isinstance(derecho,int):
                        derecho = derecho +1
                        return [izquierdo,derecho]
                    elif isinstance(izquierdo, float) and isinstance(derecho,float):
                        return [izquierdo,derecho]
                    else:
                        err= Errores(str(izquierdo)+":"+str(derecho),"Semántico", "Error en el rango", self.fila,self.columna)
                        tree.insertError(err)
                        return err
                except:
                    err= Errores(str(izquierdo)+":"+str(derecho),"Semántico", "Error en el rango", self.fila,self.columna)
                    tree.insertError(err)
                    return err

    def getNodo(self):
        return super().getNodo()