from TablaSimbolos.Tipos import Tipo_Acceso
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
        
        if self.valor == None:
            #SE CREA UN OBJETO TIPO SIMBOLO PARA AGREGARLO A LA TABLA ACTUAL
            simbolo = Simbolo(self.id,None,self.acceso,self.fila,self.columna)
            resultado = table.AddSimbolo(simbolo)
            # SE VERIFICA QUE DEVOLVIÓ SIMBOLO
            if isinstance(resultado,Errores):
                tree.insertError(resultado)
                return "Hay un error"
            return "Hecho"
        else:
            #SE EJECUTA EL VALOR DE LA VARIABLE
            self.valor = self.valor.ejecutar(tree,table)
            #SE CREA UN OBJETO TIPO SIMBOLO PARA AGREGARLO A LA TABLA ACTUAL
            simbolo = Simbolo(self.id,self.valor,self.acceso,self.fila,self.columna)

            resultado = table.AddSimbolo(simbolo)
            # SE VERIFICA QUE DEVOLVIÓ SIMBOLO
            if isinstance(resultado,Errores):
                tree.insertError(resultado)
                return "Hay un error"
            return "Hecho"

    
    def getNodo(self):
        return super().getNodo()
