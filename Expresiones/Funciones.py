from TablaSimbolos.Tipos import Tipo_FuncionAritmetica
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
            print(self.valor1)
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
    def getNodo(self):
        return super().getNodo()