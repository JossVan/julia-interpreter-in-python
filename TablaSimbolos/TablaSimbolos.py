
from TablaSimbolos.Tipos import Tipo_Acceso
from TablaSimbolos.Errores import Errores

class TablaSimbolos:
    def __init__(self,nombre, anterior = None):
        self.tabla = {} 
        self.anterior = anterior
        self.nombre = nombre

    def AddSimbolo(self, simbolo):    
        if simbolo.getID() in self.tabla :
            self.tabla[simbolo.getID()] = simbolo
        else:
            self.tabla[simbolo.getID()] = simbolo
            return None

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
                tablaActual.tabla[simbolo.getID()].setValor(simbolo.getValor())
                return None          
            else:
                tablaActual = tablaActual.anterior
        
        self.tabla[simbolo.getID()] = simbolo
        return None