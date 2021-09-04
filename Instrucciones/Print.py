from TablaSimbolos.Tipos import Tipo_Print
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
            print((self.contenido))
            resultado = self.contenido.ejecutar(tree,table)
            return resultado
        if self.tipo == Tipo_Print.PRINTLN:
            print(type(self.contenido))
            resultado = self.contenido.ejecutar(tree,table)
            return resultado+"\n"
    def getNodo(self):
        return super().getNodo()
