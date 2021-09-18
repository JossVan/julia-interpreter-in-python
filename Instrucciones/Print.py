from TablaSimbolos.Errores import Errores
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Tipos import Tipo_Primitivas, Tipo_Print
from Abstractas.Objeto import TipoObjeto
from Abstractas.NodoAST import NodoAST

class Print(NodoAST):

    def __init__(self, tipo, contenido, fila, columna):
        self.tipo = tipo 
        self.contenido= contenido
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):

        if self.tipo == Tipo_Print.PRINT:  
            if self.contenido != "":
                for instrucciones in self.contenido:
                    resultado = instrucciones.ejecutar(tree,table)
                    if isinstance(resultado,list):
                        array = self.imprime(tree,table,resultado,[])
                        if len(array) == 0:
                            tree.updateConsola(str(resultado))
                        else:
                            tree.updateConsola(str(array))
                    elif isinstance(resultado, NodoAST):
                        val = resultado.ejecutar(tree,table)
                        if not isinstance(val,list):
                            tree.updateConsola(str(val))
                        else:
                            array = self.imprime(tree,table,resultado,[])
                            if array !=None:
                                if len(array) == 1:
                                    tree.updateConsola(str(array[0])+" ")
                            else:
                                tree.updateConsola(str(array))
                    elif isinstance(resultado, Errores):
                        return resultado
                    else:
                        tree.updateConsola(str(resultado))
        if self.tipo == Tipo_Print.PRINTLN:
            if self.contenido != "":
                for instrucciones in self.contenido:
                    resultado = instrucciones.ejecutar(tree,table)
                    if isinstance(resultado,list):
                        array = self.imprime(tree,table,resultado,[])
                        if len(array) == 0:
                            tree.updateConsola(str(resultado))
                        else:
                            tree.updateConsola(str(array))
                    elif isinstance(resultado, NodoAST):
                        val = resultado.ejecutar(tree,table)
                        if not isinstance(val,list):
                            tree.updateConsola(str(val))
                        else:
                            array = self.imprime(tree,table,resultado,[])
                            if array !=None:
                                tree.updateConsola(str(array))
                            else:
                                tree.updateConsola(str(array))
                    elif isinstance(resultado, Errores):
                        return resultado
                    else:
                        tree.updateConsola(str(resultado))
            tree.updateConsola("\n")

    def getNodo(self):
        
        NodoNuevo = NodoArbol("Impresión")

        if self.tipo == Tipo_Print.PRINT:
            NodoNuevo.agregarHijo("Print")
        elif self.tipo == Tipo_Print.PRINTLN:
            NodoNuevo.agregarHijo("Println")
        
        for instruccion in self.contenido:
            NodoNuevo.agregarHijoNodo(instruccion.getNodo())

        return NodoNuevo
    
    
    def imprime(self,tree,table,resultado,array):

        if isinstance(resultado, list):
            for i in resultado:
                if isinstance(i, NodoAST):
                    result = i.ejecutar(tree,table)
                    self.imprime(tree,table,result,array)
                elif isinstance(i,list):
                    self.imprime(tree,table,i,array)
            return array
        elif isinstance(resultado,NodoAST):
            val = resultado.ejecutar(tree,table)
            return self.imprime(tree,table,val,array)
            
        else:
            array.append(resultado)