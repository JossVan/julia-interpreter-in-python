from Abstractas.NodoAST import NodoAST

class Lista_impresion(NodoAST):

    def __init__(self, lista ,impresion, fila, columna):
        self.impresion = impresion
        self.lista = lista
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        valor = ""
        if isinstance(self.lista, NodoAST):
            valor+=self.lista.ejecutar(tree,table)

        if isinstance(self.impresion,NodoAST):
            valor+= self.impresion.ejecutar(tree,table)
        return valor
    def getNodo(self):
        return super().getNodo()