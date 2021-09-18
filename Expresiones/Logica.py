from TablaSimbolos.Errores import Errores
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Tipos import Tipo_Logico, Tipo_Relacional
from Abstractas.NodoAST import NodoAST

class Logica(NodoAST):

    def __init__(self, operador1, operador2, tipooperacion, fila, columna):
        self.operador1=operador1
        self.operador2 = operador2
        self.tipooperacion = tipooperacion
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        
        if self.operador1!=None and self.operador2!=None:
            resultado1= self.operador1.ejecutar(tree,table)
            resultado2= self.operador2.ejecutar(tree,table)
            if isinstance(resultado2,Errores) or isinstance(resultado1,Errores):
                return Errores("Operación no permitida", "Semántico", "F", self.fila,self.columna)
            if self.tipooperacion == Tipo_Logico.AND:
                if resultado1 and resultado2:
                    return True
                return False
            if self.tipooperacion == Tipo_Logico.OR:
                if resultado1 or resultado2:
                    return True
                return False
        if self.operador2== None and self.operador1 !=None:
            resultado1= self.operador1.ejecutar(tree,table)

            if self.tipooperacion == Tipo_Logico.DIFERENTE:
                if not resultado1:
                    return True
                return False

    def getNodo(self):
        NuevoNodo = NodoArbol("Lógicas")
        if self.tipooperacion == Tipo_Logico.AND:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo("AND")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Logico.OR:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo("OR")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Logico.DIFERENTE:
            NuevoNodo.agregarHijo("!")
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())

        return NuevoNodo
            