from TablaSimbolos.Tipos import Tipo_Acceso, Tipo_Dato
from TablaSimbolos.Errores import Errores
from os import error
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Abstractas.NodoAST import NodoAST

class Asignacion(NodoAST):

    def __init__(self, acceso, id, valor, tipo, fila, columna):
        self.acceso = acceso
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.fila = fila 
        self.columna = columna

    def ejecutar(self, tree, table):
        
        if self.tipo == None:
            if self.valor == None:
                #SE CREA UN OBJETO TIPO SIMBOLO PARA AGREGARLO A LA TABLA ACTUAL
                simbolo = Simbolo(self.id,None,self.acceso,self.fila,self.columna)
                table.actualizarSimbolo(simbolo)
            else:
                print(self.valor)
                #SE EJECUTA EL VALOR DE LA VARIABLE
                
                valor = self.valor.ejecutar(tree,table)
                #SE CREA UN OBJETO TIPO SIMBOLO PARA AGREGARLO A LA TABLA ACTUAL
                simbolo = Simbolo(self.id,valor,self.acceso,self.fila,self.columna)
                table.actualizarSimbolo(simbolo)
        else:
            print("ESTÁ EN ASIGNACIÓN CON TIPO")
            if self.valor != None:
                tipo =""
                self.valor = self.valor.ejecutar(tree,table)
                print(type(self.tipo))
                if self.tipo == Tipo_Dato.CADENA:
                    if isinstance(self.valor,str):
                        simbolo = Simbolo(self.id,self.valor,self.acceso,self.fila,self.columna)
                        table.AddSimbolo(simbolo)
                    else:
                        error = Errores(self.valor,"Semántico","La variable declarada debe ser una cadena",self.fila,self.columna)
                        tree.insertError(error)
                if self.tipo == Tipo_Dato.BOOLEANO:
                    if isinstance(self.valor, bool):
                        simbolo = Simbolo(self.id,self.valor,self.acceso,self.fila,self.columna)
                        table.AddSimbolo(simbolo)
                    else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser tipo booleano",self.fila,self.columna)
                        tree.insertError(error)
                if self.tipo == Tipo_Dato.CARACTER:
                     if isinstance(self.valor, chr):
                        simbolo = Simbolo(self.id,self.valor,self.acceso,self.fila,self.columna)
                        table.AddSimbolo(simbolo)
                     else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser de tipo caracter",self.fila,self.columna)
                        tree.insertError(error)
                if self.tipo == Tipo_Dato.DECIMAL:
                    if isinstance(self.valor, float):
                        simbolo = Simbolo(self.id,self.valor,self.acceso,self.fila,self.columna)
                        table.AddSimbolo(simbolo)
                    else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser de tipo Float64",self.fila,self.columna)
                        tree.insertError(error)
                if self.tipo == Tipo_Dato.ENTERO:
                    print(self.valor)
                    if isinstance(self.valor, int):
                        simbolo = Simbolo(self.id,self.valor,self.acceso,self.fila,self.columna)
                        table.AddSimbolo(simbolo)
                    else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser de tipo Int64",self.fila,self.columna)
                        tree.insertError(error)
    def getNodo(self):
        return super().getNodo()
