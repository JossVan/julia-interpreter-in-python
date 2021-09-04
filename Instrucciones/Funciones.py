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
        return super().ejecutar(tree, table)