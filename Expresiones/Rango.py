from Abstractas.NodoArbol import NodoArbol
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
                    if isinstance(self.izquierdo, list):
                        for izq in self.izquierdo:
                            izquierdo = izq.ejecutar(tree,table)
                            arreglo = []
                            for cont in izquierdo:
                                if isinstance(cont, NodoAST):
                                    valor = cont.ejecutar(tree,table)
                                    arreglo.append(valor)
                                else:
                                    return Errores("Operación desconocida", "Semántico","F",self.fila,self.columna)
                            return arreglo
                    elif isinstance(self.izquierdo, NodoAST):
                        izquierdo = self.izquierdo.ejecutar(tree,table)
                        if isinstance(izquierdo, list):
                            '''for izq in izquierdo:
                            return izq'''
                            return izquierdo
                        elif isinstance(izquierdo, NodoAST):
                            izq = izquierdo.ejecutar(tree,table)
                            return izq
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
                        return Rango(self.id,izquierdo,derecho,self.fila,self.columna)
                    elif isinstance(izquierdo, float) and isinstance(derecho,float):
                        return Rango(self.id,izquierdo,derecho,self.fila,self.columna)
                    else:
                        err= Errores(str(izquierdo)+":"+str(derecho),"Semántico", "Error en el rango", self.fila,self.columna)
                        tree.insertError(err)
                        return err
                except:
                    err= Errores("rango","Semántico", "Error en el rango", self.fila,self.columna)
                    tree.insertError(err)
                    return err

    def getNodo(self):
        nodoNuevo = NodoArbol("Rango")
        if self.izquierdo != None and self.derecho != None:
            if isinstance(self.izquierdo,list):
                for izq in self.izquierdo:
                    nodoNuevo.agregarHijoNodo(izq.getNodo())
            else:
                nodoNuevo.agregarHijoNodo(self.izquierdo.getNodo())
            nodoNuevo.agregarHijo(":")
            nodoNuevo.agregarHijoNodo(self.derecho.getNodo())
        elif self.derecho == None:
            if isinstance(self.izquierdo,list):
                for inst in self.izquierdo:
                    nodoNuevo.agregarHijoNodo(inst.getNodo())
            elif isinstance(self.izquierdo,NodoAST):
                nodoNuevo.agregarHijoNodo(self.izquierdo.getNodo())
        return nodoNuevo