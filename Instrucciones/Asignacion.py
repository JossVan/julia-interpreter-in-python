from Abstractas.NodoAST import NodoAST

class Asignacion(NodoAST):

    def __init__(self, acceso, id, valor, tipo, fila, columna):
        self.acceso = acceso
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        self.valor = self.valor.ejecutar(tree, table)
        print(self.valor)
        return self.valor
    
    def getNodo(self):
        return super().getNodo()
