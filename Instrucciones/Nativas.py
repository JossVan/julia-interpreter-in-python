from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Tipos import Tipo_Dato, Tipo_Primitivas
from Abstractas.NodoAST import NodoAST

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
    
                self.valor = self.valor.ejecutar(tree,table)
                if self.tipo == Tipo_Dato.BOOLEANO:
                    try:
                        if isinstance(self.valor,str):
                            return bool(self.valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a booleano"
                elif self.tipo == Tipo_Dato.CADENA:
                    print(self.valor)
                    try:
                        if isinstance(self.valor,str):
                            return str(self.valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a cadena"
                elif self.tipo == Tipo_Dato.ENTERO:
                    try:
                        if isinstance(self.valor, str):
                            return int(self.valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a Int64"
                elif self.tipo == Tipo_Dato.DECIMAL:
                    try:
                        if isinstance(self.valor, str):
                            return float(self.valor)
                        return "El segundo parámetro debe ser una cadena"
                    except ValueError:
                        return "Error al castear a Float64"
                elif self.tipo == Tipo_Dato.CARACTER:
                    try:
                        if isinstance(self.valor, str):
                            return chr(self.valor)
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

class Nativas_SinTipo(NodoAST):

    def __init__(self, funcion, valor, fila, columna):
        self.funcion = funcion
        self.valor = valor
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):

        self.valor = self.valor.ejecutar(tree,table)
        print("ESTA EN NATIVAS SIN TIPO")
        if self.funcion == Tipo_Primitivas.FLOAT:
            try:
                return float(self.valor)
            except ValueError:
                return "El parámetro debe ser un número entero"
        elif self.funcion == Tipo_Primitivas.STRING:
            return str(self.valor)
        elif self.funcion == Tipo_Primitivas.TYPEOF:
            if(isinstance(self.valor, bool)):
                return "Bool"
            elif (isinstance(self.valor,int)):
                return "Int64"
            elif(isinstance(self.valor,float)):
                return "Float64"
            elif(isinstance(self.valor,str)):
                return "String"
        elif self.funcion == Tipo_Primitivas.TRUNC:   
            if isinstance(self.valor,int) or isinstance(self.valor,float):
                return int(self.valor)
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
                    return len(val)
    def getNodo(self):
        NodoNuevo = NodoArbol("Funciones_Arreglos")
        if self.funcion == Tipo_Primitivas.LENGTH:
            NodoNuevo.agregarHijo("Length")
            NodoNuevo.agregarHijoNodo(self.valor.getNodo())
        return NodoNuevo