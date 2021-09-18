from Expresiones.Arreglos import Arreglos
from Expresiones.Array import Array
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Tipos import Tipo_Dato, Tipo_Primitivas
from Abstractas.NodoAST import NodoAST
import numpy as np
class Nativas_conTipo(NodoAST):

    def __init__(self, funcion, tipo, valor,  fila, columna):
        self.funcion = funcion 
        self.tipo = tipo 
        self.valor = valor 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):

        if self.funcion == Tipo_Primitivas.PARSE:
 
            if self.tipo != None:
    
                valor = self.valor.ejecutar(tree,table)
                if self.tipo == Tipo_Dato.BOOLEANO:
                    try:
                        if isinstance(valor,str):
                            return bool(self.valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a booleano"
                elif self.tipo == Tipo_Dato.CADENA:
                    try:
                        if isinstance(valor,str):
                            return valor
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a cadena"
                elif self.tipo == Tipo_Dato.ENTERO:
                    try:
                        if isinstance(valor, str):
                            return int(valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a Int64"
                elif self.tipo == Tipo_Dato.DECIMAL:
                    try:
                        if isinstance(valor, str):
                            return float(valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a Float64"
                elif self.tipo == Tipo_Dato.CARACTER:
                    try:
                        if isinstance(valor, str):
                            return chr(valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a char"
        elif self.funcion == Tipo_Primitivas.TRUNC:
            if self.tipo == Tipo_Dato.ENTERO:
                self.valor = self.valor.ejecutar(tree,table)
                return int(self.valor)
            else:
                return "El primer parametro debe ser Int64" 
    def getNodo(self):
        NodoNuevo = NodoArbol("Funciones_Nativas")

        if self.funcion == Tipo_Primitivas.PARSE:
            NodoNuevo.agregarHijo("Parse")
        elif self.funcion == Tipo_Primitivas.TRUNC:
            NodoNuevo.agregarHijo("Trunc")
        
        if self.tipo == Tipo_Dato.CADENA:
            NodoNuevo.agregarHijo("String")
        elif self.tipo == Tipo_Dato.CARACTER:
            NodoNuevo.agregarHijo("Char")
        elif self.tipo == Tipo_Dato.ENTERO:
            NodoNuevo.agregarHijo("Int64")
        elif self.tipo == Tipo_Dato.DECIMAL:
            NodoNuevo.agregarHijo("Float64")
        elif self.tipo == Tipo_Dato.BOOLEANO:
            NodoNuevo.agregarHijo("Bool")
        NodoNuevo.agregarHijoNodo(self.valor.getNodo())
        return NodoNuevo
class Nativas_SinTipo(NodoAST):

    def __init__(self, funcion, valor, fila, columna):
        self.funcion = funcion
        self.valor = valor
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):

        valor = self.valor.ejecutar(tree,table)
        if self.funcion == Tipo_Primitivas.FLOAT:
            try:
                return float(valor)
            except ValueError:
                return "El parámetro debe ser un número entero"
        elif self.funcion == Tipo_Primitivas.STRING:
            return str(valor)
        elif self.funcion == Tipo_Primitivas.TYPEOF:
            if(isinstance(valor, bool)):
                return "Bool"
            elif (isinstance(valor,int)):
                return "Int64"
            elif(isinstance(valor,float)):
                return "Float64"
            elif(isinstance(valor,str)):
                return "String"
        elif self.funcion == Tipo_Primitivas.TRUNC:   
            if isinstance(valor,int) or isinstance(valor,float):
                return int(valor)
            else:
                return "El primer parametro debe ser un número flotante"
        else:
            return "HAY UN ERROR"
    def getNodo(self):
        NodoNuevo = NodoArbol("Funciones_Nativas")

        if self.funcion == Tipo_Primitivas.FLOAT:
            NodoNuevo.agregarHijo("Float")
        elif self.funcion == Tipo_Primitivas.STRING:
            NodoNuevo.agregarHijo("String")
        elif self.funcion == Tipo_Primitivas.TYPEOF:
            NodoNuevo.agregarHijo("Typeof")
        elif self.funcion == Tipo_Primitivas.TRUNC:
            NodoNuevo.agregarHijo("Trunc")
        NodoNuevo.agregarHijoNodo(self.valor.getNodo())

        return NodoNuevo

class Pilas(NodoAST):
    def __init__(self, funcion, id, valor, fila, columna):
        self.funcion = funcion
        self.id = id
        self.valor = valor
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        if self.funcion == Tipo_Primitivas.LENGTH:
            if isinstance(self.valor, NodoAST):
                val = self.valor.ejecutar(tree,table)
                if isinstance(val,list):   
                    tam = self.getLen(val)
                    if tam != None:
                        return tam       
                    array = np.array(val)
                    return array.size
        elif self.funcion == Tipo_Primitivas.PUSH:
            val = self.id.ejecutar(tree,table)
            if isinstance(val,list):
                if isinstance(val[0],list):
                    if isinstance(self.valor,list):
                        val[0].append(self.valor[0])
                    else:
                        val.append(self.valor)
                    table.actualizarValor(self.id.id,val)  
                else:                
                    val.append(self.valor)
                    table.actualizarValor(self.id.id,val)
            return val
        elif self.funcion == Tipo_Primitivas.POP:
            result = self.id.ejecutar(tree,table)
            retorno = []
            if result != None:
                if isinstance(result,list):
                    if isinstance(result[0],list):
                        tam = int(len(result[0])-1)
                        retorno = result[0][tam]
                        result[0].pop(tam)
                        table.actualizarValor(self.id.id,result)
                    else:
                        tam = int(len(result)-1)
                        retorno = result[tam]
                        result.pop(tam)
                        table.actualizarValor(self.id.id,result)

                return retorno
                
    def getNodo(self):
        NodoNuevo = NodoArbol("Funciones_Arreglos")
        if self.funcion == Tipo_Primitivas.LENGTH:
            NodoNuevo.agregarHijo("Length")
            NodoNuevo.agregarHijoNodo(self.valor.getNodo())
        return NodoNuevo
    
    def getLen(self,array):

        if isinstance(array,list):
            for i in array:
                if isinstance(i, Arreglos):
                    return i.getLength()
                elif isinstance(i,list):
                    self.getLen(i)
        elif isinstance(array, Arreglos):
            return array.getLength()
        else :
            None