from Expresiones.Arreglos import Arreglos
from Abstractas.NodoArbol import NodoArbol
from Instrucciones.Return import Return
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from TablaSimbolos.Errores import Errores
from Abstractas.NodoAST import NodoAST

class Llamadas(NodoAST):

    def __init__(self, id, parametros, fila, columna):
        self.id = id 
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
        
    def ejecutar(self, tree, table):
        funcion = tree.getFuncion(self.id)
        struct = tree.getStruct(self.id)
        if funcion == None and struct == None:
            err = Errores(self.id, "Semántico", "Instruccion no reconocida", self.fila, self.columna)
            tree.insertError(err)
            return
        elif funcion != None and struct == None:
            NuevaTabla = TablaSimbolos(self.id,table)
            if self.parametros != None:
                if len(funcion.parametros) == len(self.parametros):
                    contador = 0
                    for parametro in self.parametros:
                        valor = parametro.ejecutar(tree,table)
                        variable = funcion.parametros[contador].id
                        simbolo = Simbolo(variable,valor,self.id,self.fila,self.columna,"No definido")
                        NuevaTabla.addSimboloLocal(simbolo)
                        tree.agregarTS(self.id,simbolo)
                        contador = contador+1

                    resultado = funcion.ejecutar(tree,NuevaTabla)
                    if isinstance(resultado,Return):
                        return resultado.valor
                    elif isinstance(resultado, Errores):
                        return resultado
                else :
                    err = Errores(self.id, "Semántico", "No coinciden los parámetros de llamada", self.fila,self.columna)
                    tree.insertError(err)
            else:
                resultado = funcion.ejecutar(tree,NuevaTabla)
                if isinstance(resultado,Return):
                    return resultado.valor
        elif struct != None:
            #HAY UNA ASIGNACION DE TIPO STRUCT
            elementos = struct.ejecutar(tree,table)
            if len(elementos) == len(self.parametros):
                contador = 0
                tablita = TablaSimbolos(self.id)
                for par in  self.parametros:
                    verificar = elementos[contador].verificarTipo(tree, table, par)
                    if  verificar:
                        if isinstance(par,NodoAST):
                            par = par.ejecutar(tree,table)
                        tablita.tabla[elementos[contador].id] = par
                    elif isinstance(verificar,Errores):
                        return verificar
                    contador = contador +1
                return tablita

    def getNodo(self):
        
        NodoPadre = NodoArbol("Llamada")
        Nodoid = NodoArbol("Identificador")
        Nodopar = NodoArbol("Parámetros")
        Nodoid.agregarHijo(self.id)
        NodoPadre.agregarHijoNodo(Nodoid)
        NodoPadre.agregarHijo("(")
        cont = 1
        if self.parametros != None:
            for parametro in self.parametros:
                Nodopar.agregarHijoNodo(parametro.getNodo())
                if cont < len(self.parametros):
                    Nodopar.agregarHijo(",")
                    cont= cont+1
            NodoPadre.agregarHijoNodo(Nodopar)
        NodoPadre.agregarHijo(")")
        return NodoPadre