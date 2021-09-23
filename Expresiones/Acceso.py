from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Structs import Struct
from TablaSimbolos.Errores import Errores
from Expresiones.Identificador import Identificador
from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST

class Acceso(NodoAST):

    def __init__(self, lista,fila, columna):
        self.lista = lista
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        
        if self.lista != None:
            result = self.lista[0].ejecutar(tree,table)
            if result != None and isinstance(result,TablaSimbolos):
                contador = 0
                for item in self.lista:
                    if contador > 0:
                        if isinstance(item,Identificador):
                            ID = item.id
                            result = self.buscar(result,ID) 
                            if result == None:
                                error = Errores(item,"Semántico","No se ha encontrado el acceso",self.fila,self.columna)
                                tree.insertError(error)
                                return error
                    contador = contador +1

                return result

    def verificar(self,tree,table, valor):
        if self.lista != None:
            result = self.lista[0].ejecutar(tree,table)
            nombre = result.nombre
            if result != None:
                contador = 0
                for item in self.lista:
                    if contador > 0 and contador< (len(self.lista)-1):
                        if isinstance(item,Identificador):
                            ID = item.id
                            result = self.buscar(result,ID) 
                            if result == None:
                                error = Errores(item,"Semántico","No se ha encontrado el acceso",self.fila,self.columna)
                                tree.insertError(error)
                                return error
                    contador = contador +1
            struct = tree.getStruct(nombre)
            if struct!=None:
                if isinstance(struct,Struct):
                    mutable = struct.mutables()
                    if mutable:
                        if isinstance(result,TablaSimbolos):
                            ultimo= self.lista[len(self.lista)-1].id
                            val = valor.ejecutar(tree,table)
                            result.tabla[ultimo] = val
                    else:
                        error = Errores(nombre,"Semántico","El struct no es mutable, no se puede modificar",self.fila,self.columna)
                        tree.insertError(error)
                        return error

    def buscar(self,ts,id):

        if id in ts.tabla:
            return ts.tabla[id]         

    def getNodo(self):
        
        NodoNuevo = NodoArbol("ACCESO")
        contador = 1
        for acceso in self.lista :
            
            if isinstance(acceso,NodoAST):
                NodoNuevo.agregarHijoNodo(acceso.getNodo())
                if contador < len(self.lista):
                    NodoNuevo.agregarHijo(".")
        return NodoNuevo