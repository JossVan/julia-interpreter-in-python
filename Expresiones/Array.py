from Abstractas.NodoAST import NodoAST
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Errores import Errores
class Array(NodoAST):

    def __init__(self, id, posicion, fila, columna):
        self.id = id 
        self.posicion = posicion
        self.fila = fila 
        self.columna = columna
    

    def ejecutar(self, tree, table):
        
        id = self.id
        self.id = self.id.lower()
        resultado = table.BuscarIdentificador(self.id)
        if resultado == None:
            tree.insertError(Errores(id,"Semántico","No definida", self.fila,self.columna))
            return
        b = resultado.getValor()
        
        if isinstance(self.posicion, list):
            
            for posi in self.posicion:
                if isinstance(posi, NodoAST):
                    valor = posi.ejecutar(tree,table)
                    if isinstance(b, list):
                        if valor -1 >= 0:
                            nodito = b[valor-1]
                            if isinstance(nodito, NodoAST):
                                nodito = nodito.ejecutar(tree,table)
                                return nodito
                            return nodito
                            
                        else : 
                            print("ERROR, DESBORDAMIENTO")
                    else:
                        print (" ERROR SEMÁNTICO ")
                elif isinstance(posi, int):
                    if isinstance(b,list):
                        if posi-1 >=0:
                            nodito = b[posi-1]
                            if isinstance(nodito, NodoAST):
                                nodito = nodito.ejecutar(tree,table)
                                return nodito
                            return nodito
                        else :
                            print ("ERROR DESBORDAMIENTO")
                else:
                    print("ERROR SEMÁNTICO ")

    def actualizar(self, valor, tree, table):
        id = self.id
        self.id = self.id.lower()
        posi = 0
        if isinstance(self.posicion, list):
            for pos in self.posicion:
                posi = pos.ejecutar(tree,table)
        val = valor.ejecutar(tree,table)
        resultado = table.actualizarValorPosicion(val, posi, self.id)

        if resultado == None:
            tree.insertError(Errores(id,"Semántico","No definida", self.fila,self.columna))
            return
    
    def getNodo(self):
        nodoPadre = NodoArbol("Array")
        nodoId = NodoArbol("Identificador")
        nodoId.agregarHijo(self.id)
        nodoPadre.agregarHijoNodo(nodoId)
        nodopos = NodoArbol("Posición")
        if isinstance(self.posicion,list):
            for pos in self.posicion:
                nodopos.agregarHijoNodo(pos.getNodo())         
        nodoPadre.agregarHijoNodo(nodopos)
        return nodoPadre