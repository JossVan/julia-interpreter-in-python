from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Abstractas.NodoAST import NodoAST
from Instrucciones.Break import Break
class While(NodoAST):

    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion= condicion
        self.instrucciones = instrucciones
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        
        while True:
            nuevaTabla = TablaSimbolos("While",table)
            condicion = self.condicion.ejecutar(tree,nuevaTabla)
            if (condicion):
                for instruccion in self.instrucciones:
                    resp = instruccion.ejecutar(tree,nuevaTabla)
                    if isinstance(resp, Break):
                        return None
            else:
                break
    def getNodo(self):
        return super().getNodo()