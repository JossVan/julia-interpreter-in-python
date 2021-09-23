from Expresiones.Acceso import Acceso
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Abstractas.NodoArbol import NodoArbol
from Expresiones.Array import Array
from Expresiones.Identificador import Identificador
from Expresiones.Arreglos import Arreglos
from TablaSimbolos.Tipos import Tipo_Acceso, Tipo_Dato
from TablaSimbolos.Errores import Errores
from TablaSimbolos.Simbolo import Simbolo
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
        id =""
        if isinstance(self.id,Identificador):
            id = self.id.id
        elif isinstance(self.id, Array):
            self.id.actualizar(self.valor,tree,table)
            return
        elif isinstance(self.id, str):
            id = self.id
        elif isinstance(self.id, Acceso):
            id = self.id.verificar(tree,table,self.valor)
            return
        '''else:
            err = Errores(self.id,"Semántico", "el valor de asignación debe ser un identificador", self.fila,self.columna)
            tree.insertError(err)'''
        if self.tipo == None:
            if self.valor == None:
                simbolo = table.BuscarIdentificador(id)
                if simbolo != None:
                    if self.acceso == Tipo_Acceso.GLOBAL:
                        table.actualizarSimboloGlobal(simbolo)
                    else:
                        table.actualizarSimbolo(simbolo)
                    tree.agregarTS(id,simbolo)
                else:   
                    simbolo = Simbolo(id, None, self.acceso,self.fila,self.columna, "Ninguno")
                    if self.acceso == Tipo_Acceso.GLOBAL:
                        table.actualizarSimboloGlobal(simbolo)
                    else:
                        table.actualizarSimbolo(simbolo)
                    tree.agregarTS(id,simbolo)
            else:
                if isinstance(self.valor,list):
                    for val in self.valor :
                        if isinstance(val, Arreglos):
                            valor = val.ejecutar(tree,table)
                            if isinstance(valor,Errores):
                                return valor
                            simbolo = Simbolo(id, valor, self.acceso,self.fila,self.columna,"Arreglo")
                            if self.acceso == Tipo_Acceso.GLOBAL:
                                table.actualizarSimboloGlobal(simbolo)
                            else:
                                table.actualizarSimbolo(simbolo)
                            tree.agregarTS(id,simbolo)
                        else:
                            print("ERROR")
                else:
                    valor = self.valor.ejecutar(tree,table)
                    if isinstance(valor,Errores):
                        return valor
                    elif isinstance(valor, TablaSimbolos):
                        simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna, "STRUCT")
                    else:
                        simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna, "Primitivo")
                    if self.acceso == Tipo_Acceso.GLOBAL:           
                        table.actualizarSimboloGlobal(simbolo)
                    else:
                        table.actualizarSimbolo(simbolo)
                    tree.agregarTS(id,simbolo)
        else:
            
            if self.valor != None:
                if self.tipo == Tipo_Dato.CADENA:
                    if isinstance(self.valor,NodoAST):
                        valor = self.valor.ejecutar(tree,table)
                        if isinstance(valor, str):
                            simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna, "String")
                            if self.acceso == Tipo_Acceso.GLOBAL:
                                table.actualizarSimboloGlobal(simbolo)
                            else:
                                table.actualizarSimbolo(simbolo)
                            tree.agregarTS(id,simbolo)
                        else:
                            err = Errores(str(valor),"Semántico","Los tipos no coinciden", self.fila,self.columna)
                            tree.insertError(err)
                            return err
                    elif isinstance(self.valor, list):
                        for val in self.valor :
                            if isinstance(val, Arreglos):
                                print("ES UN ARREGLO")
                    else:
                        error = Errores(self.valor,"Semántico","La variable declarada debe ser una cadena",self.fila,self.columna)
                        tree.insertError(error)
                elif self.tipo == Tipo_Dato.BOOLEANO:
                    if isinstance(self.valor,NodoAST):
                        valor = self.valor.ejecutar(tree,table)
                        if isinstance(valor, bool):
                            simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna,"Bool")
                            if self.acceso == Tipo_Acceso.GLOBAL:
                                table.actualizarSimboloGlobal(simbolo)
                            else:
                                table.actualizarSimbolo(simbolo)
                            tree.agregarTS(id,simbolo)
                        else:
                            err = Errores(str(valor),"Semántico","Los tipos no coinciden", self.fila,self.columna)
                            tree.insertError(err)
                            return err
                    elif isinstance(self.valor, list):
                        for val in self.valor :
                            if isinstance(val, Arreglos):
                                print("ES UN ARREGLO")
                    else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser tipo booleano",self.fila,self.columna)
                        tree.insertError(error)
                elif self.tipo == Tipo_Dato.CARACTER:
                     if isinstance(self.valor,NodoAST):
                        valor = self.valor.ejecutar(tree,table)
                        if isinstance(valor, chr):
                            simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna,"Char")
                            if self.acceso == Tipo_Acceso.GLOBAL:
                                table.actualizarSimboloGlobal(simbolo)
                            else:
                                table.actualizarSimbolo(simbolo)
                            tree.agregarTS(id,simbolo)
                        else:
                            err = Errores(str(valor),"Semántico","Los tipos no coinciden", self.fila,self.columna)
                            tree.insertError(err)
                            return err
                     elif isinstance(self.valor, list):
                        for val in self.valor :
                            if isinstance(val, Arreglos):
                                print("ES UN ARREGLO")  
                     else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser de tipo caracter",self.fila,self.columna)
                        tree.insertError(error)
                elif self.tipo == Tipo_Dato.DECIMAL:
                    if isinstance(self.valor,NodoAST):
                        valor = self.valor.ejecutar(tree,table)
                        if isinstance(valor, float):
                            simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna, "Float64")
                            if self.acceso == Tipo_Acceso.GLOBAL:
                                table.actualizarSimboloGlobal(simbolo)
                            else:
                                table.actualizarSimbolo(simbolo)
                            tree.agregarTS(id,simbolo)
                        else:
                            err = Errores(str(valor),"Semántico","Los tipos no coinciden", self.fila,self.columna)
                            tree.insertError(err)
                            return err
                    elif isinstance(self.valor, list):
                        for val in self.valor :
                            if isinstance(val, Arreglos):
                                print("ES UN ARREGLO")
                    else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser de tipo Float64",self.fila,self.columna)
                        tree.insertError(error)
                elif self.tipo == Tipo_Dato.ENTERO:
                    if isinstance(self.valor,NodoAST):
                        valor = self.valor.ejecutar(tree,table)
                        if isinstance(valor, int):
                            simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna, "Int64")
                            if self.acceso == Tipo_Acceso.GLOBAL:
                                table.actualizarSimboloGlobal(simbolo)
                            else:
                                table.actualizarSimbolo(simbolo)
                            tree.agregarTS(id,simbolo)
                        else:
                            err = Errores(str(valor),"Semántico","Los tipos no coinciden", self.fila,self.columna)
                            tree.insertError(err)
                            return err
                    elif isinstance(self.valor, list):
                        for val in self.valor :
                            if isinstance(val, Arreglos):
                                print("ES UN ARREGLO")
                    else: 
                        error = Errores(self.valor,"Semántico","El valor de la variable debe ser de tipo Int64",self.fila,self.columna)
                        tree.insertError(error)
                        return error
                else :
                    result = tree.getStruct(self.tipo)
                    if result == None:
                        error = Errores(self.valor,"Semántico","El tipo de la variable no existe",self.fila,self.columna)
                        tree.insertError(error)
                        return error
                    else:
                        valor = self.valor.ejecutar(tree,table)
                        if isinstance(valor,Errores):
                            return valor
                        if isinstance(valor, TablaSimbolos):
                            simbolo = Simbolo(id,valor,self.acceso,self.fila,self.columna, "STRUCT")
                        if self.acceso == Tipo_Acceso.GLOBAL:           
                            table.actualizarSimboloGlobal(simbolo)
                        else:
                            table.actualizarSimbolo(simbolo)
                        tree.agregarTS(id,simbolo)

    def getNodo(self):
        NodoNuevo = NodoArbol("Asignación")
        if self.tipo == Tipo_Acceso.GLOBAL:
            NodoNuevo.agregarHijo("Global")
        elif self.tipo == Tipo_Acceso.LOCAL:
            NodoNuevo.agregarHijo("Local")

        if isinstance(self.id,NodoAST):
            NodoNuevo.agregarHijoNodo(self.id.getNodo())
        elif isinstance(self.id,str):
            NodoNuevo.agregarHijo(self.id)
        if isinstance(self.valor, NodoAST):
            NodoNuevo.agregarHijoNodo(self.valor.getNodo())
        elif isinstance(self.valor, list):
            for inst in self.valor:
                NodoNuevo.agregarHijoNodo(inst.getNodo())
        if self.tipo == Tipo_Dato.BOOLEANO:
            NodoNuevo.agregarHijo("::")
            NodoNuevo.agregarHijo("Bool")
        elif self.tipo == Tipo_Dato.CADENA:
            NodoNuevo.agregarHijo("::")
            NodoNuevo.agregarHijo("String")
        elif self.tipo == Tipo_Dato.ENTERO:
            NodoNuevo.agregarHijo("::")
            NodoNuevo.agregarHijo("Int64")
        elif self.tipo == Tipo_Dato.DECIMAL:
            NodoNuevo.agregarHijo("::")
            NodoNuevo.agregarHijo("Float64")
        elif self.tipo == Tipo_Dato.CARACTER:
            NodoNuevo.agregarHijo("::")
            NodoNuevo.agregarHijo("Char")
        
        NodoNuevo.agregarHijo(";")
        return NodoNuevo

