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
            for instrucciones in self.contenido:
                resultado = str(instrucciones.ejecutar(tree,table))
                tree.updateConsola(resultado)
        if self.tipo == Tipo_Print.PRINTLN:
            for instrucciones in self.contenido:
                resultado = str(instrucciones.ejecutar(tree,table))
                tree.updateConsola(resultado)
            tree.updateConsola("\n")

    def getNodo(self):
        return super().getNodo()
