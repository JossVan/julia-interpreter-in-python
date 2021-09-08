from enum import Enum

class Tipo_Aritmetico(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    MODAL = 5
    POTENCIA = 6


class Tipo_Dato(Enum):
    ENTERO =1
    DECIMAL = 2
    CADENA = 3
    CARACTER = 4
    BOOLEANO = 5
    NULO = 6
    STRUCT = 7
    ARRAY = 8

class Tipo_Relacional(Enum):
    MENOR =1
    MAYOR = 2
    MENOR_IGUAL = 3
    MAYOR_IGUAL = 4
    IGUAL = 5
    DIFERENTE = 6

class Tipo_Logico(Enum):
    OR = 1
    AND = 2
    DIFERENTE = 3

class Tipo_FuncionAritmetica(Enum):
    log10 = 1
    seno = 2
    coseno = 3
    tangente = 4
    sqrt = 5
    uppercase = 6
    lowercase = 7
    log = 8

class Tipo_Primitivas(Enum):

    TRUNC = 1
    PARSE = 2
    FLOAT = 3
    STRING = 4
    TYPEOF = 5
    PUSH = 6
    POP = 7
    LENGTH = 8

class Tipo_Print(Enum):

    PRINT = 1
    PRINTLN = 2

class Tipo_Acceso(Enum):
    GLOBAL = 1
    LOCAL = 2
    NONE = 3