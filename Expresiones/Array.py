from Abstractas.NodoAST import NodoAST
from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Errores import Errores
from Expresiones.Arreglos import Arreglos
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
                    h = self.desanidar(tree,table,b)
                    nodito = h[array[0]-1]
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
                if pos1 >= 0 and pos2 >=0:
                    nodito = b[pos1][pos2]
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
                if pos1 >= 0 and pos2 >=0 and pos3 >=0:
                    nodito = b[pos1][pos2][pos3]
                    if isinstance(nodito, NodoAST):
                        nodito = nodito.ejecutar(tree,table)
                        return nodito
                    elif isinstance(nodito,list):
                        lista = []
                        for v in nodito :
                            if isinstance(v,NodoAST):
                                valor = v.ejecutar(tree,table)
                                lista.append(valor)
                            else:
                                lista.append(v)
                        return lista
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
            h = self.desanidar(tree,table,traerValor.valor)
            if len(array) == 1:
                nueva = []
                if isinstance(valor, list):
                    for i in valor:
                        if isinstance(i,Arreglos):
                            v = i.contenido
                            if isinstance(v,list):
                                for val in v:
                                    if isinstance(val,NodoAST):
                                        valorcito = val.ejecutar(tree,table)
                                        nueva.append(valorcito)
                            else:
                                nueva.append(v)
                        else:
                            nueva.append(i)
                    valor = nueva
                h[posi-1].append(valor)
                traerValor.valor = h
                table.actualizarValor(self.id,traerValor.valor)
            return traerValor.valor
        


        
    def getNodo(self):
        nodoPadre = NodoArbol("Array")
        nodoId = NodoArbol("Identificador")
        nodoId.agregarHijo(self.id)
        nodoPadre.agregarHijoNodo(nodoId)
        nodopos = NodoArbol("Posición")
        nodopos.agregarHijo("[")
        if isinstance(self.posicion,list):
            for pos in self.posicion:
                nodopos.agregarHijoNodo(pos.getNodo())     
        nodopos.agregarHijo("]")    
        nodoPadre.agregarHijoNodo(nodopos)
        return nodoPadre
    
    
    def desanidar(self,tree,table,item):
        contador = 0
        if isinstance(item,list):
            for i in item:
                if isinstance(i,list):
                    self.desanidar(tree,table,i)
                elif isinstance(i,Arreglos):
                    result = i.ejecutar(tree,table)
                    
                    item[contador] = result 

                contador = contador +1
            return item
            
    def ejecutarMatriz(self,tree,table,array,nuevo):

        if isinstance(array,list):
            for arreglo in array:
                if isinstance(arreglo,Arreglos):
                    contenido = arreglo.ejecutar(tree,table)
                    nuevo.append(contenido)
                elif isinstance(arreglo,list):
                    self.ejecutarMatriz(tree,table,arreglo,nuevo)
        elif isinstance(array, Arreglos):
            contenido = array.ejecutar(tree,table)
            nuevo.append(contenido)

        return nuevo