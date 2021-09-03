from Abstractas.NodoAST import NodoAST

class Nativas_conTipo(NodoAST):

    def __init__(self, funcion, tipo, valor,  fila, columna):
        self.funcion = funcion 
        self.tipo = tipo 
        self.valor = valor 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()


class Nativas_SinTipo(NodoAST):

    def __init__(self, funcion, valor, fila, columna):
        self.funcion = funcion
        self.valor = valor
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()

class Pilas(NodoAST):
    def __init__(self, funcion, id, valor, fila, columna):
        self.funcion = funcion
        self.id = id
        self.valor = valor
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        return super().ejecutar(tree, table)
    
    def getNodo(self):
        return super().getNodo()
