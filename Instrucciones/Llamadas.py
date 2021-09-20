from Abstractas.NodoArbol import NodoArbol
from Instrucciones.Return import Return
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from TablaSimbolos.Errores import Errores
from Abstractas.NodoAST import NodoAST

class Llamadas(NodoAST):

    def __init__(self, id, parametros, fila, columna):
        self.id = id 
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
        
    def ejecutar(self, tree, table):
        funcion = tree.getFuncion(self.id)
        
        if funcion == None:
            err = Errores(self.id, "Semántico", "La función no existe", self.fila, self.columna)
            tree.insertError(err)
        else:
            NuevaTabla = TablaSimbolos(self.id,table)
            if self.parametros != None:
                if len(funcion.parametros) == len(self.parametros):
                    contador = 0
                    for parametro in self.parametros:
                        valor = parametro.ejecutar(tree,table)
                        variable = funcion.parametros[contador].id
                        simbolo = Simbolo(variable,valor,self.id,self.fila,self.columna,"No definido")
                        NuevaTabla.addSimboloLocal(simbolo)
                        tree.agregarTS(self.id,simbolo)
                        contador = contador+1

                    resultado = funcion.ejecutar(tree,NuevaTabla)
                    if isinstance(resultado,Return):
                        return resultado.valor
                    elif isinstance(resultado, Errores):
                        return resultado
                else :
                    err = Errores(self.id, "Semántico", "No coinciden los parámetros de llamada", self.fila,self.columna)
                    tree.insertError(err)
            else:
                resultado = funcion.ejecutar(tree,NuevaTabla)
                if isinstance(resultado,Return):
                    return resultado.valor

    def getNodo(self):
        
        NodoPadre = NodoArbol("Llamada")
        Nodoid = NodoArbol("Identificador")
        Nodopar = NodoArbol("Parámetros")
        Nodoid.agregarHijo(self.id)
        NodoPadre.agregarHijoNodo(Nodoid)
        NodoPadre.agregarHijo("(")
        cont = 1
        for parametro in self.parametros:
            Nodopar.agregarHijoNodo(parametro.getNodo())
            if cont < len(self.parametros):
                Nodopar.agregarHijo(",")
                cont= cont+1
        if self.parametros != None:
            NodoPadre.agregarHijoNodo(Nodopar)
        NodoPadre.agregarHijo(")")
        return NodoPadre