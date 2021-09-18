from TablaSimbolos.Errores import Errores
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
            valor1 = self.valor1.ejecutar(tree,table)

            if self.funcion == Tipo_FuncionAritmetica.lowercase:
                if isinstance(valor1,str):
                    return valor1.lower()
                err = Errores(valor1,"Semántico","Valor no permitido, debe ser una cadena", self.fila,self.columna)
                tree.insertError(err)
                return err
            elif self.funcion == Tipo_FuncionAritmetica.uppercase:
                if isinstance(valor1,str):
                    return valor1.upper()
                err = Errores(valor1,"Semántico","Valor no permitido, debe ser una cadena", self.fila,self.columna)
                tree.insertError(err)
                return err
            elif self.funcion == Tipo_FuncionAritmetica.log10:
                try:
                    return round(math.log(valor1,10))
                except:
                    err = Errores(valor1,"Semántico","Valor no permitido, debe ser un número", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.funcion == Tipo_FuncionAritmetica.seno:
                try:
                    return math.sin(valor1)
                except:
                    err = Errores(valor1,"Semántico","Valor no permitido, debe ser un número", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.funcion == Tipo_FuncionAritmetica.coseno:
                try:
                    return math.cos(valor1)
                except:
                    err = Errores(valor1,"Semántico","Valor no permitido, debe ser un número", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.funcion == Tipo_FuncionAritmetica.tangente:
                try:
                    return math.tan(valor1)
                except:
                    err = Errores(valor1,"Semántico","Valor no permitido, debe ser un número", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.funcion == Tipo_FuncionAritmetica.sqrt:
                try:
                    return math.sqrt(valor1)
                except:
                    err = Errores(valor1,"Semántico","Valor no permitido, debe ser un número", self.fila,self.columna)
                    tree.insertError(err)
                    return err
        elif self.valor2!=None and self.valor1 !=None:
            valor1 = self.valor1.ejecutar(tree,table)
            valor2 = self.valor2.ejecutar(tree,table)
            if self.funcion == Tipo_FuncionAritmetica.log:
                return math.log(valor2,valor1)
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