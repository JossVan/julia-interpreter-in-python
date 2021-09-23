from TablaSimbolos.Errores import Errores
from TablaSimbolos.Tipos import Tipo_Dato
from Abstractas.NodoArbol import NodoArbol
from Abstractas.NodoAST import NodoAST

class Elemento(NodoAST):

    def __init__(self, id, tipo, fila, columna):
        self.id = id
        self.tipo = tipo
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        print("ejecutar elemento")

    def verificarTipo(self, tree, tabla, valor):
        if self.tipo == None:
            return True
        if isinstance(self.tipo,Tipo_Dato):
            if self.tipo == Tipo_Dato.BOOLEANO:
                if isinstance(valor,NodoAST):
                    valor = valor.ejecutar(tree,tabla)
                if isinstance(valor,bool):
                    return True
                else:
                    err = Errores(valor,"Semántico","El valor del item debe ser booleano",self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.tipo == Tipo_Dato.CADENA:
                if isinstance(valor,NodoAST):
                    valor = valor.ejecutar(tree,tabla)
                if isinstance(valor,str):
                    return True
                else:
                    err = Errores(valor,"Semántico","El valor del item debe ser String",self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.tipo == Tipo_Dato.CARACTER:
                if isinstance(valor,NodoAST):
                    valor = valor.ejecutar(tree,tabla)
                if isinstance(valor,chr):
                    return True
                else:
                    err = Errores(valor,"Semántico","El valor del item debe ser tipo char",self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.tipo == Tipo_Dato.DECIMAL:
                if isinstance(valor,NodoAST):
                    valor = valor.ejecutar(tree,tabla)
                if isinstance(valor,float):
                    return True
                else:
                    err = Errores(valor,"Semántico","El valor del item debe ser booleano",self.fila,self.columna)
                    tree.insertError(err)
                    return err
            elif self.tipo == Tipo_Dato.ENTERO:
                if isinstance(valor,NodoAST):
                    valor = valor.ejecutar(tree,tabla)
                if isinstance(valor,int):
                    return True
                else:
                    err = Errores(valor,"Semántico","El valor del item debe ser booleano",self.fila,self.columna)
                    tree.insertError(err)
                    return err
        else:
            tipo = tree.getStruct(self.tipo)
            if (tipo ==None):
                err = Errores(self.tipo,"Semántico","El tipo asignado no existe",self.fila,self.columna)
                tree.insertError(err)
                return err
            else:
                return tipo
    
    def getNodo(self):
        
        NodoNuevo = NodoArbol("ELEMENTO")
        NodoNuevo.agregarHijo(self.id)
        
        if self.tipo != None:
            if isinstance(self.tipo,Tipo_Dato):
                if self.tipo == Tipo_Dato.BOOLEANO:
                    NodoNuevo.agregarHijo("Bool")
                elif self.tipo == Tipo_Dato.CADENA:
                    NodoNuevo.agregarHijo("String")
                elif self.tipo == Tipo_Dato.CARACTER:
                    NodoNuevo.agregarHijo("Char")
                elif self.tipo == Tipo_Dato.DECIMAL:
                    NodoNuevo.agregarHijo("Float64")
                elif self.tipo == Tipo_Dato.ENTERO:
                    NodoNuevo.agregarHijo("Int64")
            else:
                NodoNuevo.agregarHijo(self.tipo)
        return NodoNuevo