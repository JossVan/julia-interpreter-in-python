from Abstractas.Objeto import TipoObjeto
from Abstractas.NodoArbol import NodoArbol
from Objetos.Primitivos import Primitivo
from Abstractas.NodoAST import NodoAST

class Constante(NodoAST):

    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        if isinstance(self.valor,Primitivo):
            if self.valor.tipo == TipoObjeto.CADENA:
                return self.valor.toString()
            elif self.valor.tipo == TipoObjeto.ENTERO:
                return self.valor.getEntero()
            elif self.valor.tipo == TipoObjeto.DECIMAL:
                return self.valor.getFloat()
            elif self.valor.tipo == TipoObjeto.BOOLEANO:
                return self.valor.getBoolean()
            elif self.valor.tipo == TipoObjeto.NEGATIVO:
                resultado = self.valor.valor.ejecutar(tree,table)
                return resultado * (-1)
            return "F"
    
    def getNodo(self):
        NuevoNodo = NodoArbol("Constante")
        if self.valor.tipo == TipoObjeto.CADENA:
            NuevoNodo.agregarHijo(self.valor.toString())
        elif self.valor.tipo == TipoObjeto.ENTERO:
            NuevoNodo.agregarHijo(str(self.valor.getEntero()))
        elif self.valor.tipo == TipoObjeto.DECIMAL:
            NuevoNodo.agregarHijo(str(self.valor.getFloat()))
        elif self.valor.tipo == TipoObjeto.BOOLEANO:
            NuevoNodo.agregarHijo(str(self.valor.getBoolean()))
        elif self.valor.tipo == TipoObjeto.NEGATIVO:
            if isinstance(self.valor, NodoAST):
                NuevoNodo.agregarHijoNodo("-"+ self.valor.getNodo())
        return NuevoNodo