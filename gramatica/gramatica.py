import re

reservadas = {
     'nothing' : 'R_NOTHING',
     'Int64' : 'R_INT64',
     'Float64' : 'R_FLOAT64',
     'String' : 'R_STRING',
     'Char' : 'R_CHAR',
     'Bool' : 'R_BOOL',
     'struct' : 'R_STRUCT',
     'uppercase' : 'R_UPPERCASE',
     'lowercase' : 'R_LOWERCASE',
     'log' : 'R_LOG',
     'log10' : 'R_LOG10',
     'sin' : 'R_SIN',
     'cos' : 'R_COS',
     'tan' : 'R_TAN',
     'sqrt' : 'R_SQRT',
     'print' : 'R_PRINT',
     'println' : 'R_PRINTLN',
     'global': 'R_GLOBAL',
     'local' : 'R_LOCAL',
     'function' : 'R_FUNCTION',
     'if' : 'R_IF',
     'elseif' : 'R_ELSEIF',
     'else' : 'R_ELSE',
     'for' : 'R_FOR',
     'while' : 'R_WHILE',
     'trunc' : 'R_TRUNC',
     'parse' : 'R_PARSE',
     'float' : 'R_FLOAT',
     'string' : 'R_SSTRING',
     'typeof' : 'R_TYPEOF',
     'push' : 'R_PUSH',
     'pop' : 'R_POP',
     'length' : 'R_LENGTH',
     'end' : 'R_END',
     'in' : 'R_IN',
     'return' : 'R_RETURN',
     'break' : 'R_BREAK',
     'continue' : 'R_CONTINUE',
     'mutable': 'R_MUTABLE',
     'true' : 'R_TRUE',
     'false' : 'R_FALSE'
}

tokens  = [
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODAL',
    'POTENCIA',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'COMA',
    'PUNTO',
    'AND',
    'OR',
    'DIFERENTE',
    'DOSPUNTOS',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID',
    'DOLAR'
] + list(reservadas.values())

# Tokens
t_PTCOMA    = r';'
t_CORIZQ   = r'\['
t_CORDER   = r'\]'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_MODAL     = r'%'
t_POTENCIA  = r'\^'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_MENORIGUAL= r'<='
t_MAYORIGUAL= r'>='
t_COMA      = r','
t_PUNTO     = r'.'
t_DOSPUNTOS = r':'
t_OR       = r'\|\|'
t_AND       = r'&&'
t_DIFERENTE = r'!'
t_DOLAR     = r'\$'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'\#\=(.|\n)*\=\#'
    t.lexer.lineno += t.value.count('\n')
    print(t.value)
# Comentario simple // ...

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
#t_ignore = " \r"
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    print(t)

def t_IGNORAR(t):
    r'\ |\t|\r'
    global columna
    if t.value == '\r':
       print("salto de linea")    
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()
lexer.lineno = 1

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO','MODAL'),
    ('left', 'POTENCIA'),
    ('right','UMENOS'),
    )

# Definición de la gramática

from Expresiones.Aritmetica import Aritmetica
from TablaSimbolos.Tipos import Tipo_Aritmetico, Tipo_Dato, Tipo_Logico, Tipo_Relacional, Tipo_FuncionAritmetica, Tipo_Primitivas, Tipo_Print
from Abstractas.Objeto import TipoObjeto
from Expresiones.Funciones import Funciones_matematicas
from Expresiones.Constante import Constante
from Objetos.Primitivos import Primitivo
from Expresiones.Identificador import Identificador
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Expresiones.Unaria import Unaria
from Instrucciones.Nativas import Nativas_conTipo,Nativas_SinTipo, Pilas
from Instrucciones.Print import Print
def p_inicio(t):
    '''INICIO : INICIO FUNCIONES
            |   INICIO INSTRUCCIONES'''

    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    print (t[0])
def p_iniciofi(t):
    '''INICIO   : FUNCIONES
                | INSTRUCCIONES'''
    t[0] = t[1]
    
def p_instrucciones(t):
    '''INSTRUCCIONES    : INSTRUCCIONES IFS
                        | INSTRUCCIONES FORS
                        | INSTRUCCIONES WHILES
                        | INSTRUCCIONES ASIGNACION
                        | INSTRUCCIONES I
                        | INSTRUCCIONES LLAMADAS
                        | INSTRUCCIONES NATIVAS
                        | INSTRUCCIONES STRUCTS'''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instruccionesI(t):
    '''INSTRUCCIONES :    IFS
                        | FORS
                        | WHILES
                        | ASIGNACION
                        | I
                        | LLAMADAS
                        | NATIVAS
                        | STRUCTS'''
    t[0]=t[1]

def p_impresion(t):

    '''I : R_PRINT PARIZQ IMPRESION PARDER PTCOMA'''
    t[0] = Print(Tipo_Print.PRINT, t[3],t.lineno(1), 1)

def p_println(t):
    'I : R_PRINTLN PARIZQ IMPRESION PARDER PTCOMA'
    t[0] = Print(Tipo_Print.PRINTLN, t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_contImpresion(t):
    'IMPRESIONES : IMPRESIONES COMA IMPRESION'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_contimpresiones(t):
    'IMPRESIONES : IMPRESION'
    t[0] = t[1]

def p_contimpresionCont(t):
    '''IMPRESION    : E
                    | ARREGLOS
                    | NATIVAS'''
    t[0]=t[1]

def p_cont_impresionDolar(t):
    '''IMPRESION : DOLAR PARIZQ E PARDER
                 | DOLAR PARIZQ ARREGLOS PARDER
                 | DOLAR PARIZQ NATIVAS PARDER'''
    
def p_arreglos(t):
    'ARREGLOS : CORIZQ LISTAS CORDER'

def p_arreglos2(t):
    'ARREGLOS : CORIZQ LISTAS CORDER CORIZQ LISTAS CORDER'

def p_listas(t):
    'LISTAS : LISTAS COMA LISTA'

def p_listasp(t):
    'LISTAS : LISTA'

def p_lista(t):
    '''LISTA : E
            | NATIVAS
            | ARREGLOS
            | LLAMADAS'''
    t[0]=t[1]      
def p_asignaciones(t):
    '''ASIGNACION : R_GLOBAL ID IGUAL LISTA DOSPUNTOS DOSPUNTOS TIPO PTCOMA
                  | R_LOCAL ID IGUAL LISTA DOSPUNTOS DOSPUNTOS TIPO PTCOMA'''
def p_asignacionesp(t):
    'ASIGNACION : ID IGUAL LISTA DOSPUNTOS DOSPUNTOS TIPO PTCOMA'

def p_asginacionesp2(t):
    '''ASIGNACION : R_GLOBAL ID IGUAL LISTA PTCOMA
                  | R_LOCAL ID IGUAL LISTA PTCOMA'''

def p_asignacionesp3(t):
    '''ASIGNACION : R_GLOBAL ID PTCOMA
                  | R_LOCAL ID PTCOMA'''

def p_tipo(t):
    '''TIPO : R_NOTHING
            | R_INT64
            | R_FLOAT64
            | R_STRING
            | R_CHAR
            | R_BOOL'''

    if (t[1] == 'nothing'):
        t[0] = Tipo_Dato.NULO
    elif(t[1] == 'Int64'):
        t[0] = Tipo_Dato.ENTERO
    elif( t[2] == 'Float64'):
        t[0] = Tipo_Dato.DECIMAL
    elif(t[2] == 'String'):
        t[0] = Tipo_Dato.CADENA
    elif(t[2] == 'Char'):
        t[0] == Tipo_Dato.CARACTER
    elif(t[2] == 'Bool'):
        t[0] == Tipo_Dato.BOOLEANO

def p_llamadas(t):
    'LLAMADAS : ID PARIZQ LISTAS PARIZQ PTCOMA'

def p_llamadassinparametro(t):
    'LLAMADAS : ID PARIZQ PARDER PTCOMA'


def p_expresiones(t):
    '''E    : E MAS E 
            | E MENOS E
            | E POR E
            | E DIVIDIDO E
            | E MODAL E
            | E POTENCIA E'''
    if( t[2]== '+'):
        Aritmetica(t[1], Tipo_Aritmetico.SUMA, t[2], t.lineno(2), find_column(input, t.slice[2]))
    elif( t[2] == '-' ):
        Aritmetica(t[1], Tipo_Aritmetico.RESTA, t[2], t.lineno(2), find_column(input, t.slice[2]))
    elif(t[2] == '*'):
        Aritmetica(t[1], Tipo_Aritmetico.MULTIPLICACION, t[2], t.lineno(2), find_column(input, t.slice[2]))
    elif(t[2] == '/'):
        Aritmetica(t[1], Tipo_Aritmetico.DIVISION, t[2], t.lineno(2), find_column(input, t.slice[2]))
    elif(t[2] == '^'):
        Aritmetica(t[1], Tipo_Aritmetico.POTENCIA, t[2], t.lineno(2), find_column(input, t.slice[2]))
    elif(t[2] == '%'):
        Aritmetica(t[1], Tipo_Aritmetico.MODAL, t[2], t.lineno(2), find_column(input, t.slice[2]))
        
def p_expresion_unaria(t):
    'E : MENOS E %prec UMENOS'
    

def p_expresionespar(t):
    'E : PARIZQ E PARDER'
    t[0] = t[2]

def p_expresionesesp(t):
    '''E : R_LOG10 PARIZQ E PARDER'''  
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.log10, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_seno(t):
    'E : R_SIN PARIZQ E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.seno, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_coseno(t):
    'E : R_COS PARIZQ E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.coseno, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_tangente(t):
    'E : R_TAN PARIZQ E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.tangente, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_sqrt(t):
    'E : R_SQRT PARIZQ E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.sqrt, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_upper(t):
    'E : R_UPPERCASE PARIZQ E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.uppercase, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_lower(t):
    'E : R_LOWERCASE PARIZQ E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.lowercase, t[3], None, t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_log(t):
    'E : R_LOG PARIZQ E COMA E PARDER'
    t[0] = Funciones_matematicas(Tipo_FuncionAritmetica.log, t[3], t[5], t.lineno(2), find_column(input,t.slice[2]))

def p_expresiones_decimal(t):
    'E : DECIMAL'
    t[0] = Constante(Primitivo(TipoObjeto.DECIMAL,t[1]), t.lineno(2), find_column(input, t.slice[2]))
def p_expresiones_entero(t):
    'E : ENTERO'
    t[0] = Constante(Primitivo(TipoObjeto.ENTERO, t[1]), t.lineno(2), find_column(input, t.slice[2]))

def p_expresiones_booleanas(t):
    '''E : R_TRUE
        | R_FALSE'''
    t[0] = Constante(Primitivo(TipoObjeto.BOOLEANO, t[1]), t.lineno(2), find_column(input, t.slice[2]))

def p_expresiones_cadena(t):
    'E : CADENA'
    t[0] = Constante(Primitivo(TipoObjeto.CADENA, t[1]), t.lineno(1), 1)
    
def p_expresiones_id(t):
    'E : ID'
    t[0] = Identificador(t[1],t.lineno(1), find_column(input, t.slice[2]))

def p_expresiones_relacionales(t):
    ''' RE :  RE MENQUE RE
            | RE MAYQUE RE
            | RE IGUALQUE RE
            | RE NIGUALQUE RE
            | RE MENORIGUAL RE
            | RE MAYORIGUAL RE'''
    
    if(t[2] == '>'):
        t[0] = Relacional(t[1],t[3],Tipo_Relacional.MAYOR,t.lineno(2), find_column(input, t.slice[2]))
    elif(t[2] == '<'):
        t[0] = Relacional(t[1],t[3],Tipo_Relacional.MENOR,t.lineno(2), find_column(input, t.slice[2]))
    elif(t[3] == '=='):
        t[0] = Relacional(t[1],t[3],Tipo_Relacional.IGUAL,t.lineno(2), find_column(input, t.slice[2]))
    elif(t[3] == '!='):
        t[0] = Relacional(t[1],t[3],Tipo_Relacional.DIFERENTE,t.lineno(2), find_column(input, t.slice[2]))
    elif(t[3] == '<='):
        t[0] = Relacional(t[1],t[3],Tipo_Relacional.MENOR_IGUAL,t.lineno(2), find_column(input, t.slice[2]))
    elif(t[3] == '>='):
        t[0] = Relacional(t[1],t[3],Tipo_Relacional.MAYOR_IGUAL,t.lineno(2), find_column(input, t.slice[2]))

def p_expresionesE(t):
    'RE : E'
    t[0] = t[1]
def p_expresiones_logicas(t):
    '''LO :   LO AND LO
            | LO OR LO'''
    if(t[2] == '&&'):
        t[0] = Logica(t[1],t[3],Tipo_Logico.AND,t.lineno(1), find_column(input, t.slice[2]))
    elif(t[2] == '||'):
        t[0] = Logica(t[1],t[3],Tipo_Logico.OR,t.lineno(1), find_column(input, t.slice[2]))
    
def p_expresiones_logicas_diferente(t):
    'LO : DIFERENTE LO'
    if(t[1] == '!'):
        t[0] = Logica(t[2],None,Tipo_Relacional.DIFERENTE,t.lineno(1), find_column(input, t.slice[1]))

def p_expresiones_logicas_re(t):
    'LO : RE'
    t[0] = t[1]

def p_nativas(t):
    '''NATIVAS :  R_PARSE PARIZQ TIPO COMA LISTA PARDER
                | R_TRUNC PARIZQ TIPO COMA LISTA PARDER'''
    
    if(t[1]=='parse'):
        t[0] = Nativas_conTipo(Tipo_Primitivas.PARSE,t[3],t[5],t.lineno(2), find_column(input, t.slice[2]))
    elif(t[1] == 'trunc'):
        t[0] = Nativas_conTipo(Tipo_Primitivas.TRUNC,t[3],t[5],t.lineno(2), find_column(input, t.slice[2]))

def p_nativasp(t):
    '''NATIVAS :  R_FLOAT   PARIZQ LISTA PARDER
                | R_SSTRING PARIZQ LISTA PARDER
                | R_TYPEOF  PARIZQ LISTA PARDER'''
    if(t[1]=='float'):
        t[0] = Nativas_SinTipo(Tipo_Primitivas.FLOAT,t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif(t[1] == 'string'):
        t[0] = Nativas_SinTipo(Tipo_Primitivas.STRING,t[3], t.lineno(2), find_column(input, t.slice[2]))
def p_nativaspush(t):
    ' NATIVAS : R_PUSH  DIFERENTE PARIZQ ID COMA E PARDER'
    id = Identificador(t[4],t.lineno(2), find_column(input, t.slice[2]))
    t[0] = Pilas(Tipo_Primitivas.PUSH, id, t[6], t.lineno(2), find_column(input, t.slice[2]))

def p_nativaspop(t):
    'NATIVAS : R_POP DIFERENTE PARIZQ ID PARDER'
    id = Identificador(t[4],t.lineno(2), find_column(input, t.slice[2]))
    t[0] = Pilas(Tipo_Primitivas.POP, id, None, t.lineno(2), find_column(input, t.slice[2]))

def p_nativas_length(t):
    'NATIVAS : ID PUNTO R_LENGTH'
    id = Identificador(t[4],t.lineno(2), find_column(input, t.slice[2]))
    t[0] = Pilas(Tipo_Primitivas.LENGTH, id, None,t.lineno(2), find_column(input, t.slice[2]))
def p_returns(t):
    'RETURN : R_RETURN LISTA'

def p_returnUnico(t):
    'RETURN : R_RETURN'

def p_funciones(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ LISTAS PARDER INSTRUCCIONES R_END PTCOMA'

def p_funciones_return(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ LISTAS PARDER INSTRUCCIONES RETURN R_END PTCOMA'

def p_funciones_parametros_vacia(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ LISTAS PARDER  R_END PTCOMA'

def p_funciones_vacia_return(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ LISTAS PARDER RETURN R_END PTCOMA'

def p_funciones_proce(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ  PARDER INSTRUCCIONES R_END PTCOMA'

def p_funciones_proc_return(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ  PARDER INSTRUCCIONES RETURN R_END PTCOMA'

def p_funciones_proc_vacia(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ  PARDER  R_END PTCOMA'

def p_funciones_proc_vacia_return(t):
    'FUNCIONES : R_FUNCTION ID PARIZQ  PARDER RETURN R_END PTCOMA'

def p_ifs(t):
    'IFS : R_IF LO INSTRUCCIONES R_END PTCOMA'
    print("paso por el if")

def p_ifs_completo(t):
    'IFS : R_IF LO INSTRUCCIONES ELSEIF R_ELSE INSTRUCCIONES R_END PTCOMA'

def p_ifs_elsevacio(t):
    'IFS : R_IF LO INSTRUCCIONES ELSEIF R_ELSE R_END PTCOMA'

def p_ifs_soloelseif(t):
    'IFS :  R_IF LO INSTRUCCIONES ELSEIF R_END PTCOMA'

def p_ifs_soloelse(t):
    'IFS : R_IF LO INSTRUCCIONES R_ELSE INSTRUCCIONES R_END PTCOMA'

def p_ifs_elsevacio_sinelseif(t):
    'IFS : R_IF LO INSTRUCCIONES R_ELSE R_END PTCOMA'

def p_ifs_solo(t):
    'IFS : R_IF LO R_END PTCOMA'
    print("pasó por el if vacío")

def p_ifs1(t):
    'IFS : R_IF LO ELSEIF R_ELSE INSTRUCCIONES R_END PTCOMA'

def p_ifs2(t):
    'IFS : R_IF LO ELSEIF R_ELSE R_END PTCOMA'

def p_ifs3(t):
    'IFS : R_IF LO R_ELSE INSTRUCCIONES R_END PTCOMA'

def p_ifs4(t):
    'IFS : R_IF LO R_ELSE R_END PTCOMA'

def p_elseifs(t):
    'ELSEIF : ELSEIF R_ELSEIF INSTRUCCIONES'

def p_elseifs1(t):
    'ELSEIF : ELSEIF R_ELSEIF'

def p_elseifs2(t):
    'ELSEIF : R_ELSEIF INSTRUCCIONES'

def p_elseifs3(t):
    'ELSEIF : R_ELSEIF'

def p_instrucciones_loop(t):
    '''INSTRUCCIONES_LOOP :   INSTRUCCIONES_LOOP IFS
                            | INSTRUCCIONES_LOOP FORS
                            | INSTRUCCIONES_LOOP WHILES
                            | INSTRUCCIONES_LOOP ASIGNACION
                            | INSTRUCCIONES_LOOP I
                            | INSTRUCCIONES_LOOP LLAMADAS
                            | INSTRUCCIONES_LOOP NATIVAS
                            | INSTRUCCIONES_LOOP STRUCTS
                            | INSTRUCCIONES_LOOP RETURN
                            | INSTRUCCIONES_LOOP R_BREAK
                            | INSTRUCCIONES_LOOP R_CONTINUE'''
    if t[2] != "":
       t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_loop_inst(t):
    '''INSTRUCCIONES_LOOP :   IFS
                            | FORS
                            | WHILES
                            | ASIGNACION
                            | I
                            | LLAMADAS
                            | NATIVAS
                            | STRUCTS
                            | RETURN
                            | R_BREAK
                            | R_CONTINUE'''
    t[0] = t[1]

def p_whiles(t):
    'WHILES : R_WHILE LO INSTRUCCIONES_LOOP R_END PTCOMA'

def p_whiles_vacios(t):
    'WHILES :  R_WHILE LO R_END PTCOMA'

def p_fors(t):
    'FORS : R_FOR ID R_IN RANGO INSTRUCCIONES_LOOP R_END PTCOMA'

def p_fors_vacios(t):
    'FORS : R_FOR ID R_IN RANGO  R_END PTCOMA'

def p_rango(t):
    '''RANGO :    E DOSPUNTOS E
                | E
                | ID CORIZQ E DOSPUNTOS E CORDER
                | ARREGLOS'''

def p_structs(t):
    'STRUCTS : R_MUTABLE R_STRUCT ID ELEMENTOS R_END PTCOMA'

def p_structs2(t):
    'STRUCTS : R_STRUCT ID ELEMENTOS PTCOMA'

def p_structs_mutables(t):
    'STRUCTS : R_MUTABLE R_STRUCT ID R_END PTCOMA'

def p_structs_vacios(t):
    'STRUCTS : R_STRUCT ID R_END PTCOMA'

def p_elementos(t):
    'ELEMENTOS : ELEMENTOS COMA ELEMENTO'

def p_elementos_elemento(t):
    'ELEMENTOS : ELEMENTO'

def p_elemento(t):
    'ELEMENTO  : ID'

def p_elemento_declaraciontipo(t):
    'ELEMENTO : ID DOSPUNTOS DOSPUNTOS TIPO'

def p_error(t):
    print("Error sintáctico en '%s'" % str(t))

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)