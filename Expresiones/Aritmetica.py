from TablaSimbolos.Tipos import Tipo_Aritmetico
from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST

class Aritmetica(NodoAST):

    def __init__(self, operador1,operacion,operador2, linea,columna):
        self.operador1 = operador1
        self.operador2 = operador2
        self.operacion = operacion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, tree, table):
        if self.operador1!=None and self.operador2!= None:
            result1 = self.operador1.ejecutar(tree,table)
            result2 = self.operador2.ejecutar(tree,table)
            if self.operacion == Tipo_Aritmetico.SUMA:
                if isinstance(result1, str) or isinstance(result2,str) and result1!=None and result2 !=None:
                    return str(result1)+str(result2)  
                elif result1 == None:
                    return "el operador: "+self.operador1.id+", es indefinido"
                elif result2 == None:
                    return "El operador: "+self.operador2.id+", es indefinido"
                else:
                    return result1+result2
            if self.operacion == Tipo_Aritmetico.RESTA:
                if result1 == None:
                    return "el operador: "+self.operador1.id+", es indefinido"
                elif result2 == None:
                    return "El operador: "+self.operador2.id+", es indefinido"
                else:
                    return result1-result2
            if self.operacion == Tipo_Aritmetico.MULTIPLICACION:
                if result1 == None:
                    return "el operador: "+self.operador1.id+", es indefinido"
                elif result2 == None:
                    return "El operador: "+self.operador2.id+", es indefinido"
                else:
                    if isinstance(result1,str) or isinstance(result2,str):
                        return str(result1)+str(result2)
                    return result1*result2
            if self.operacion == Tipo_Aritmetico.DIVISION:
                if result2==0:
                    return "No se puede dividir entre 0"
                if result1 == None:
                    return "el operador: "+self.operador1.id+", es indefinido"
                elif result2 == None:
                    return "El operador: "+self.operador2.id+", es indefinido"
                else:
                    return result1/result2
            if self.operacion == Tipo_Aritmetico.MODAL:
                if result2==0:
                    return "No se puede dividir entre 0"
                if result1 == None:
                    return "el operador: "+self.operador1.id+", es indefinido"
                elif result2 == None:
                    return "El operador: "+self.operador2.id+", es indefinido"
                else:
                    return result1%result2
            if self.operacion == Tipo_Aritmetico.POTENCIA:
                if (isinstance(result1,int) or isinstance(result1,float)) and (isinstance(result2,int) or isinstance(result2,float)):
                    return pow(result1,result2)
                elif(isinstance(result2,float) or isinstance(result2,int)):
                    cadena=""
                    for i in range(result2):
                        cadena+=result1
                    return cadena
    def getNodo(self):
        NuevoNodo = NodoArbol("Operación_Aritmetica")
        NuevoNodo.agregarHijoNodo(self.operador1.getNodo())
        if self.operacion == Tipo_Aritmetico.SUMA:
            NuevoNodo.agregarHijo("+")
        elif self.operacion == Tipo_Aritmetico.RESTA:
            NuevoNodo.agregarHijo("-")
        elif self.operacion == Tipo_Aritmetico.MULTIPLICACION:
            NuevoNodo.agregarHijo("*")
        elif self.operacion == Tipo_Aritmetico.DIVISION:
            NuevoNodo.agregarHijo("/")
        elif self.operacion == Tipo_Aritmetico.MODAL:
            NuevoNodo.agregarHijo("%")
        elif self.operacion == Tipo_Aritmetico.POTENCIA:
            NuevoNodo.agregarHijo("^")
        NuevoNodo.agregarHijoNodo(self.operador2.getNodo())
        return NuevoNodo