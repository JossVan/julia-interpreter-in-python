from TablaSimbolos.Tipos import Tipo_Aritmetico
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
            print(self.operacion)
            if self.operacion == Tipo_Aritmetico.SUMA:
                resultado = result1+result2
                return resultado
            if self.operacion == Tipo_Aritmetico.RESTA:
                return result1-result2
            if self.operacion == Tipo_Aritmetico.MULTIPLICACION:
                return result1*result2
            if self.operacion == Tipo_Aritmetico.DIVISION:
                if result2==0:
                    return "No se puede dividir entre 0"
                return result1/result2
            if self.operacion == Tipo_Aritmetico.MODAL:
                if result2==0:
                    return "No se puede dividir entre 0"
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
        return super().getNodo()