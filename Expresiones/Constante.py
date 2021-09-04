from Abstractas.Objeto import TipoObjeto
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
            return "F"
    
    def getNodo(self):
        return super().getNodo()