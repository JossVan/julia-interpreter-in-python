from Abstractas.NodoArbol import NodoArbol
from Expresiones.Rango import Rango
from Instrucciones.Continue import Continue
from TablaSimbolos.Errores import Errores
from Abstractas.Objeto import TipoObjeto
from Objetos.Primitivos import Primitivo
from Expresiones.Constante import Constante
from TablaSimbolos.Tipos import Tipo_Acceso
from Instrucciones.Asignacion import Asignacion
from Instrucciones.Break import Break
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Abstractas.NodoAST import NodoAST

class For(NodoAST):

    def __init__(self, id, rango, instrucciones, fila, columna):
        self.id = id
        self.rango = rango
        self.instrucciones = instrucciones
        self.fila = fila 
        self.columna = columna
    
    def ejecutar(self, tree, table):
        nuevaTabla= TablaSimbolos("For",table)
        self.id.ejecutar(tree,nuevaTabla)
        id = self.id.id
        rango = self.rango.ejecutar(tree,nuevaTabla)
        if isinstance(rango,Rango):
            rango1 = rango.izquierdo
            rango2 = rango.derecho
            if isinstance(rango1,int) and isinstance(rango2,int):
                for i in range(rango1,rango2):
                    #if isinstance(rango1,int):                 
                    nuevaConstante = Constante(Primitivo(TipoObjeto.ENTERO, i), self.fila, self.columna)
                    '''elif isinstance(rango1,float):
                        nuevaConstante = Constante(Primitivo(TipoObjeto.DECIMAL, i), self.fila, self.columna)
                    else:
                        return Errores((str(rango1)+","+str(rango2)),"Semántico","Rango no aceptado", self.fila,self.columna)'''
                    nuevaAsignacion = Asignacion(Tipo_Acceso.NONE,id,nuevaConstante,None, self.fila,self.columna)
                    nuevaAsignacion.ejecutar(tree,nuevaTabla)
                    for instruccion in self.instrucciones:
                        resp= instruccion.ejecutar(tree,nuevaTabla)
                        if isinstance(resp,Break):
                            return None
                        elif isinstance(resp,Continue):
                            return None
            elif isinstance(rango1,float) and isinstance(rango2,float):
                total = int(rango2-rango1)+1
                if total >0:
                    for i in range(0,total):
                        variable = rango1
                        nuevaConstante = Constante(Primitivo(TipoObjeto.DECIMAL, variable), self.fila, self.columna)
                        rango1 = rango1+1
                        nuevaAsignacion = Asignacion(Tipo_Acceso.NONE,id,nuevaConstante,None, self.fila,self.columna)
                        nuevaAsignacion.ejecutar(tree,nuevaTabla)
                        for instruccion in self.instrucciones:
                            resp= instruccion.ejecutar(tree,nuevaTabla)
                            if isinstance(resp,Break):
                                return None
                            elif isinstance(resp,Continue):
                                return None
        else:
            if isinstance(rango,int) or isinstance(rango,float):
                if isinstance(rango, int):
                    nuevaConstante = Constante(Primitivo(TipoObjeto.ENTERO, rango), self.fila, self.columna)
                else:
                    nuevaConstante = Constante(Primitivo(TipoObjeto.DECIMAL, rango), self.fila, self.columna)

                nuevaAsignacion = Asignacion(Tipo_Acceso.NONE,id,nuevaConstante,None,self.fila,self.columna)
                nuevaAsignacion.ejecutar(tree,nuevaTabla)
                if self.instrucciones != None:
                    for instruccion in self.instrucciones:
                        resp=instruccion.ejecutar(tree,nuevaTabla)
                        if isinstance(resp,Break):
                            return None
                        elif isinstance(resp,Continue):
                            return None
            else:
                for i in rango:
                    if isinstance(i, str):
                        nuevaConstante = Constante(Primitivo(TipoObjeto.CADENA, i), self.fila, self.columna)
                        nuevaAsignacion = Asignacion(Tipo_Acceso.NONE,id,nuevaConstante,None,self.fila,self.columna)
                        nuevaAsignacion.ejecutar(tree,nuevaTabla)
                    elif isinstance(i,int): 
                        nuevaConstante = Constante(Primitivo(TipoObjeto.ENTERO, i), self.fila, self.columna)
                        nuevaAsignacion = Asignacion(Tipo_Acceso.NONE,id,nuevaConstante,None,self.fila,self.columna)
                        nuevaAsignacion.ejecutar(tree,nuevaTabla)
                    if self.instrucciones != None:
                        for instruccion in self.instrucciones:
                            resp=instruccion.ejecutar(tree,nuevaTabla)
                            if isinstance(resp,Break):
                                return None
                            elif isinstance(resp, Continue):
                                return None
                
        
    def getNodo(self):
        
        NodoNuevo = NodoArbol("For")
        NodoNuevo.agregarHijoNodo(self.id.getNodo())
        NodoNuevo.agregarHijoNodo(self.rango.getNodo())
        NodoInst = NodoArbol("Instrucciones")
        for instruccion in self.instrucciones:
            NodoInst.agregarHijoNodo(instruccion.getNodo())
        NodoNuevo.agregarHijoNodo(NodoInst)
        return NodoNuevo                

        