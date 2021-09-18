
from Abstractas.NodoAST import NodoAST
from TablaSimbolos.Tipos import Tipo_Acceso
from TablaSimbolos.Errores import Errores

class TablaSimbolos:
    def __init__(self,nombre, anterior = None):
        self.tabla = {} 
        self.anterior = anterior
        self.nombre = nombre
        
    def BuscarIdentificador(self, id):            
        tablaActual = self
        while tablaActual != None:
            if id.lower() in tablaActual.tabla :
                return tablaActual.tabla[id.lower()]
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarValor(self, id, valor):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla :
                tablaActual.tabla[id].setValor(valor)
                return None          
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarSimbolo(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.getID() in tablaActual.tabla :
                tablaActual.tabla[simbolo.getID()] = simbolo
                return None          
            else:
                tablaActual = tablaActual.anterior
        
        self.tabla[simbolo.getID()] = simbolo
        return None

    def actualizarValorPosicion(self, valor, posicion, id):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla :
                if isinstance(tablaActual.tabla[id].valor, list):
                    tablaActual.tabla[id].valor[posicion-1] = valor
                    
                return "ok"          
            else:
                tablaActual = tablaActual.anterior
        return None
        
    def actualiarValorPosicionMatriz(self,valor,pos1,pos2,id,tree):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla :
                if isinstance(tablaActual.tabla[id].valor, list):
                    tab = tablaActual.tabla[id].valor
                    nuevo = []
                    if tree.getCont() > 0:
                     tablaActual.tabla[id].valor[pos1-1][pos2-1] = valor
                    else:
                        nuevo = self.retornarResultado(None,tablaActual,tab,nuevo)
                        nuevo[pos1-1][pos2-1] = valor  
                        tablaActual.tabla[id].valor = nuevo     
                        tree.aumentar()
                    return "ok"          
            else:
                tablaActual = tablaActual.anterior
        return None

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

    def addSimboloLocal(self, simbolo):
        self.tabla[simbolo.getID()] = simbolo
        return None

    def actualizarSimboloGlobal(self,simbolo):
        tablaActual = self
        while tablaActual.anterior != None:
                tablaActual = tablaActual.anterior
        i = simbolo.getID()
        tablaActual.tabla[i.lower()] = simbolo

        return None