from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Abstractas.NodoAST import NodoAST

class If(NodoAST):

    def __init__(self, condicion, instrucciones_if, instrucciones_elseif, instrucciones_else, fila, columna):
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.instrucciones_elseif = instrucciones_elseif
        self.instrucciones_else = instrucciones_else 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        condicion = self.condicion.ejecutar(tree,table)
        if(bool(condicion) == True):
            nuevaTabla = TablaSimbolos("If",table)
            for instruccion in self.instrucciones_if:
                instruccion.ejecutar(tree,nuevaTabla)
        else:
            if(self.instrucciones_else!=None):
                nuevaTabla = TablaSimbolos("else",table)
                for instruccion in self.instrucciones_else:
                    instruccion.ejecutar(tree,nuevaTabla)

        if self.instrucciones_elseif != None :
            nuevaTabla = TablaSimbolos("elseif",table)
            self.instrucciones_elseif.ejecutar(tree,nuevaTabla)
    
    def getNodo(self):
        return super().getNodo()