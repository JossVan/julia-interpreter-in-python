from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Abstractas.NodoAST import NodoAST

class If(NodoAST):

    def __init__(self, condicion, instrucciones_if, instrucciones_elseif, instrucciones_else, fila, columna):
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.instrucciones_elseif = instrucciones_elseif
        self.instrucciones_else = instrucciones_else 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        condicion = self.condicion.ejecutar(tree,table)
        if(bool(condicion) == True):
            nuevaTabla = TablaSimbolos("If",table)
            for instruccion in self.instrucciones_if:
                resp=instruccion.ejecutar(tree,nuevaTabla)
                if isinstance(resp, Continue):
                    print("PASO POR CONTINUE")
                    return resp
                elif isinstance(resp,Break):
                    return resp
        else:
            if(self.instrucciones_else!=None):
                nuevaTabla = TablaSimbolos("else",table)
                for instruccion in self.instrucciones_else:
                    resp= instruccion.ejecutar(tree,nuevaTabla)
                    if isinstance(resp, Continue):
                        break
                    elif isinstance(resp,Break):
                        return None
        if self.instrucciones_elseif != None :
            nuevaTabla = TablaSimbolos("elseif",table)
            self.instrucciones_elseif.ejecutar(tree,nuevaTabla)
    
    def getNodo(self):
        NodoPadre = NodoArbol("If")
        # Se crea un nodo para la condición y se le introduce el hijo que es la condición
        NodoCondicion = NodoArbol("Condicion")
        NodoCondicion.agregarHijoNodo(self.condicion.getNodo())
        # Se crea un nuevo nodo para las instrucciones del if
        NodoIf = NodoArbol("Instrucciones_if")
        NodoElse = NodoArbol("Instrucciones_elseif")
        if self.instrucciones_if != None:
            for instruccion_if in self.instrucciones_if:
                NodoIf.agregarHijoNodo(instruccion_if.getNodo())
        if self.instrucciones_else != None:
            for instruccion_elseif in self.instrucciones_elseif:
                NodoElse.agregarHijoNodo(instruccion_elseif.getNodo())
        NodoPadre.agregarHijoNodo(NodoCondicion)
        NodoPadre.agregarHijoNodo(NodoIf)
        if len(self.instrucciones_else)>0:
            NodoPadre.agregarHijoNodo(NodoElse)
        return NodoPadre
        