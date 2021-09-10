from TablaSimbolos.Tipos import Tipo_FuncionAritmetica
from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST
import math

class Funciones_matematicas(NodoAST):

    def __init__(self, funcion, valor1, valor2, fila, columna):
        self.funcion = funcion
        self.valor1 = valor1
        self.valor2 = valor2
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        
        if self.valor2 == None and self.valor1 != None:
            self.valor1 = self.valor1.ejecutar(tree,table)

            if self.funcion == Tipo_FuncionAritmetica.lowercase:
                if isinstance(self.valor1,str):
                    return self.valor1.lower()
                return "El parámetro debe ser una cadena lower"
            elif self.funcion == Tipo_FuncionAritmetica.uppercase:
                if isinstance(self.valor1,str):
                    return self.valor1.upper()
                return "El parámetro debe ser una cadena upper"
            elif self.funcion == Tipo_FuncionAritmetica.log10:
                try:
                    return math.log(self.valor1)
                except:
                    return "El parámetro debe ser un número"
            elif self.funcion == Tipo_FuncionAritmetica.seno:
                try:
                    return math.sin(self.valor1)
                except:
                    return "El parámetro debe ser un número"
            elif self.funcion == Tipo_FuncionAritmetica.coseno:
                try:
                    return math.cos(self.valor1)
                except:
                    return "El parámetro debe ser un número"
            elif self.funcion == Tipo_FuncionAritmetica.tangente:
                try:
                    return math.tan(self.valor1)
                except:
                    return "El parámetro debe ser un número"
            elif self.funcion == Tipo_FuncionAritmetica.sqrt:
                try:
                    return math.sqrt(self.valor1)
                except:
                    return "El parámetro debe ser un número"
        elif self.valor2!=None and self.valor1 !=None:
            self.valor1 = self.valor1.ejecutar(tree,table)
            self.valor2 = self.valor2.ejecutar(tree,table)
            if self.funcion == Tipo_FuncionAritmetica.log:
                return math.log(self.valor2,self.valor1)
    def getNodo(self):
        NuevoNodo = NodoArbol("Funciones")
        if self.funcion == Tipo_FuncionAritmetica.lowercase:
            NuevoNodo.agregarHijo("Lowercase")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.uppercase:
            NuevoNodo.agregarHijo("Uppercase")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.seno:
            NuevoNodo.agregarHijo("Sin")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.coseno:
            NuevoNodo.agregarHijo("Cos")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.tangente:
            NuevoNodo.agregarHijo("Tan")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.sqrt:
            NuevoNodo.agregarHijo("Sqrt")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.log10:
            NuevoNodo.agregarHijo("Log10")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
        elif self.funcion == Tipo_FuncionAritmetica.log:
            NuevoNodo.agregarHijo("Log")
            NuevoNodo.agregarHijoNodo(self.valor1.getNodo())
            NuevoNodo.agregarHijoNodo(self.valor2.getNodo())
        
        return NuevoNodo