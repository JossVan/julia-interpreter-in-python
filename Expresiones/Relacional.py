from TablaSimbolos.Errores import Errores
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Tipos import Tipo_Relacional
from Abstractas.NodoAST import NodoAST

class Relacional(NodoAST):

    def __init__(self, operador1, operador2, tipooperacion, fila, columna):
        self.operador1 = operador1
        self.operador2 = operador2
        self.tipooperacion = tipooperacion
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        if self.operador1!=None and self.operador2!=None:
            resultado1 = self.operador1.ejecutar(tree,table)
            resultado2 = self.operador2.ejecutar(tree,table)
            if isinstance(resultado1,Errores) or isinstance(resultado2,Errores):
                return False
            if self.tipooperacion == Tipo_Relacional.MAYOR:
                if resultado1>resultado2:
                    return True
                return False
            elif self.tipooperacion == Tipo_Relacional.MENOR:
               
                if resultado1<resultado2:
                    return True
                return False
            elif self.tipooperacion == Tipo_Relacional.MENOR_IGUAL:
                if resultado1<= resultado2:
                    return True
                return False
            elif self.tipooperacion == Tipo_Relacional.MAYOR_IGUAL:
                if resultado1>= resultado2:
                    return True
                return False
            elif self.tipooperacion == Tipo_Relacional.IGUAL:
                if resultado1 == resultado2:
                    return True
                return False
            elif self.tipooperacion == Tipo_Relacional.DIFERENTE:
                if resultado1 != resultado2:
                    return True
                return False
            
    
    def getNodo(self):
        NuevoNodo = NodoArbol("Lógicas")
        if self.tipooperacion == Tipo_Relacional.MAYOR:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo(">")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Relacional.MENOR:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo("<")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Relacional.MAYOR_IGUAL:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo(">=")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Relacional.MENOR_IGUAL:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo("<=")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Relacional.IGUAL:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo("==")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        elif self.tipooperacion == Tipo_Relacional.DIFERENTE:
            NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
            NuevoNodo.agregarHijo("!=")
            NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        return NuevoNodo
    