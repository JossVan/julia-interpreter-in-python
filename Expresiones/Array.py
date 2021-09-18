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
        array = []
        if isinstance(self.posicion, list):    
            for posi in self.posicion:
                if isinstance(posi, NodoAST):
                    valor = posi.ejecutar(tree,table)
                    array.append(valor)
                elif isinstance(posi, int):
                    array.append(valor)
                else:
                    err = Errores(posi,"Semántico","Valor no reconocido", self.fila,self.columna)
                    tree.insertError(err)
                    return err
        if len(array) == 1:
            if isinstance(b, list):
                if array[0] -1 >= 0:
                    nodito = b[array[0]-1]
                    if isinstance(nodito, NodoAST):
                        nodito = nodito.ejecutar(tree,table)
                        return nodito
                    return nodito
                    
                else : 
                    err = Errores(str(array[0]-1),"Semántico","Desbordamiento de arreglo", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            else:
                err = Errores(b,"Semántico","Valor no reconocido", self.fila,self.columna)
                tree.insertError(err)
                return err
        elif len(array) == 2:
            if isinstance(b, list):
                pos1 = array[0]-1
                pos2 = array[1]-1
                nuevo = []
                if pos1 >= 0 and pos2 >=0:
                    nuevo = self.retornarResultado(tree,table,b,nuevo)
                    nodito = nuevo[pos1][pos2]
                    if isinstance(nodito, NodoAST):
                        nodito = nodito.ejecutar(tree,table)
                        return nodito
                    return nodito  
                else : 
                    err = Errores(str(array[0]-1),"Semántico","Desbordamiento de arreglo", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            else:
                err = Errores(b,"Semántico","Valor no reconocido", self.fila,self.columna)
                tree.insertError(err)
                return err

        elif len(array) == 3:
            if isinstance(b, list):
                pos1 = array[0]-1
                pos2 = array[1]-1
                pos3 = array[2]-1
                nuevo = []
                if pos1 >= 0 and pos2 >=0 and pos3 >=0:
                    nuevo = self.retornarResultado(tree,table,b,nuevo)
                    nodito = nuevo[pos1][pos2][pos3]
                    if isinstance(nodito, NodoAST):
                        nodito = nodito.ejecutar(tree,table)
                        return nodito
                    return nodito  
                else : 
                    err = Errores(str(array[0]-1),"Semántico","Desbordamiento de arreglo", self.fila,self.columna)
                    tree.insertError(err)
                    return err
            else:
                err = Errores(b,"Semántico","Valor no reconocido", self.fila,self.columna)
                tree.insertError(err)
                return err

    def actualizar(self, valor, tree, table):
        id = self.id
        self.id = self.id.lower()
        posi = 0
        if isinstance(self.posicion, list):
            array = []
            for pos in self.posicion:
                posi = pos.ejecutar(tree,table)
                array.append(posi)
        if len(array) == 2:
            val = valor.ejecutar(tree,table)
            resultado = table.actualiarValorPosicionMatriz(val,array[0],array[1],self.id,tree)
        elif len(array) == 3:
            val = valor.ejecutar(tree,table)
            resultado = table.actualiarValorPosicionDimension3(val,array[0],array[1],array[2],self.id,tree)
        else:
            val = valor.ejecutar(tree,table)
            resultado = table.actualizarValorPosicion(val, posi, self.id)
            
        if resultado == None:
                err = Errores(id,"Semántico","Variable indefinida", self.fila,self.columna)
                tree.insertError(err)
                return err

    def insertar(self,valor,tree,table):
        #id = self.id
        self.id = self.id.lower()
        posi = 0
        if isinstance(self.posicion, list):
            array = []
            for pos in self.posicion:
                posi = pos.ejecutar(tree,table)
                array.append(posi)
        
        traerValor = table.BuscarIdentificador(self.id)
        if isinstance(traerValor.valor, list):
            if len(array) == 1:
                if isinstance(traerValor.valor[0],list):
                    if isinstance(valor,list):
                        traerValor.valor[0].append(valor[0])
                    else:
                        traerValor.valor[0].append(valor)
                    table.actualizarValor(self.id,traerValor.valor)
            return traerValor.valor
        


        
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
    
    def retornarResultado(self,tree,table, array,nuevo):
        for i in array:
            if isinstance(i, list):
                self.retornarResultado(tree,table,i,nuevo)
            elif isinstance(i, NodoAST):
                val = i.ejecutar(tree,table)
                nuevo.append(val)
        
        if isinstance(array, NodoAST):
            val= array.ejecutar(tree,table)
            nuevo.append(val)
        return nuevo