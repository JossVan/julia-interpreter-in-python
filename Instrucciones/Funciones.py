from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Return import Return
from TablaSimbolos.Errores import Errores
from Abstractas.NodoAST import NodoAST

class Funciones(NodoAST):

    def __init__(self, nombre, parametros, instrucciones, retorno, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.retorno = retorno
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        nuevaTabla = TablaSimbolos("Funcion",table) 
        for instruccion in self.instrucciones:
            resp = instruccion.ejecutar(tree,nuevaTabla)
            if isinstance(resp, Errores):
                return resp
            if isinstance(resp, Return):
                return resp
    def getNodo(self):
        
        NodoNuevo = NodoArbol("Función")
        NodoNuevo.agregarHijo(self.nombre)
        Nodopar = NodoArbol("Parámetros")
        Nodoinst = NodoArbol("Instrucciones")
        if self.parametros != None:
            for parametro in self.parametros:
                Nodopar.agregarHijoNodo(parametro.getNodo())
        for instruccion in self.instrucciones:
            Nodoinst.agregarHijoNodo(instruccion.getNodo())
        
        if self.parametros != None:
            NodoNuevo.agregarHijoNodo(Nodopar)
        if self.instrucciones != None :
            NodoNuevo.agregarHijoNodo(Nodoinst)
        
        NodoNuevo.agregarHijo("end")
        NodoNuevo.agregarHijo(";")
        return NodoNuevo