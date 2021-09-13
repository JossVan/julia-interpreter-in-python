
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