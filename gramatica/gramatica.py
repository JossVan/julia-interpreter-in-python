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
     'mutable': 'R_MUTABLE'

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
'''
from expresiones import *
from instrucciones import *'''

def p_inicio(t):
    '''INICIO : INICIO FUNCIONES
            |   INICIO INSTRUCCIONES'''
    return [0]
def p_iniciofi(t):
    '''INICIO   : FUNCIONES
                | INSTRUCCIONES'''

    t[0] = t[1]
    return [0]
def p_instrucciones(t):
    '''INSTRUCCIONES    : INSTRUCCIONES IFS
                        | INSTRUCCIONES FORS
                        | INSTRUCCIONES WHILES
                        | INSTRUCCIONES ASIGNACION
                        | INSTRUCCIONES I
                        | INSTRUCCIONES LLAMADAS
                        | INSTRUCCIONES NATIVAS
                        | INSTRUCCIONES STRUCTS'''

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

    '''I :     R_PRINT PARIZQ IMPRESION PARDER PTCOMA 
             | R_PRINTLN PARIZQ IMPRESION PARDER PTCOMA'''

    t[0] = t[3]
    
def p_contImpresion(t):
    'IMPRESION : IMPRESION COMA IMPRESION'

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

def p_expresion_unaria(t):
    'E : MENOS E %prec UMENOS'

def p_expresionespar(t):
    'E : PARIZQ E PARDER'

def p_expresionesesp(t):
    '''E    : R_LOG10 PARIZQ E PARDER
            | R_SIN PARIZQ E PARDER
            | R_COS PARIZQ E PARDER
            | R_TAN PARIZQ E PARDER
            | R_SQRT PARIZQ E PARDER
            | R_UPPERCASE PARIZQ E PARDER
            | R_LOWERCASE PARIZQ E PARDER'''  

def p_expresiones_log(t):
    'E : R_LOG PARIZQ E COMA E PARDER'

def p_expresiones_identificadores(t):
    '''E : DECIMAL
         | ENTERO
         | CADENA
         | ID'''
    t[0] = t[1]

def p_expresiones_relacionales(t):
    ''' RE :  RE MENQUE RE
            | RE MAYQUE RE
            | RE IGUALQUE RE
            | RE NIGUALQUE RE
            | RE MENORIGUAL RE
            | RE MAYORIGUAL RE'''
    print(t[1])

def p_expresionesE(t):
    'RE : E'
def p_expresiones_logicas(t):
    '''LO :   LO AND LO
            | LO OR LO'''

def p_expresiones_logicas_diferente(t):
    'LO : DIFERENTE LO'

def p_expresiones_logicas_re(t):
    'LO : RE'
    print("pasó por expresión lógica")

def p_nativas(t):
    '''NATIVAS :  R_PARSE PARIZQ TIPO COMA LISTA PARDER
                | R_TRUNC PARIZQ TIPO COMA LISTA PARDER'''

def p_nativasp(t):
    '''NATIVAS :  R_FLOAT   PARIZQ LISTA PARDER
                | R_SSTRING PARIZQ LISTA PARDER
                | R_TYPEOF  PARIZQ LISTA PARDER'''

def p_nativaspush(t):
    ' NATIVAS : R_PUSH  DIFERENTE PARIZQ ID COMA E PARDER'

def p_nativaspop(t):
    'NATIVAS : R_POP DIFERENTE PARIZQ E PARDER'

def p_nativas_length(t):
    'NATIVAS : ID PUNTO R_LENGTH'

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