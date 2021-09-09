
from TablaSimbolos.Tipos import Tipo_Acceso
from TablaSimbolos.Errores import Errores

class TablaSimbolos:
    def __init__(self,nombre, anterior = None):
        self.tabla = {} 
        self.anterior = anterior
        self.nombre = nombre

    def AddSimbolo(self, simbolo):    
        if simbolo.getID() in self.tabla :
            return Errores("Semantico", "Variable " + simbolo.identificador + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.getID()] = simbolo
            return None

    def BuscarIdentificador(self, id):            
        tablaActual = self
        contador = 0
        while tablaActual != None:
            if id.lower() in tablaActual.tabla :
                if tablaActual.tabla[id.lower()].getAmbito() == Tipo_Acceso.LOCAL and contador > 0:
                    print("Sin acceso a esa variable")
                else:
                    return tablaActual.tabla[id.lower()]
            else:
                tablaActual = tablaActual.anterior
                contador= contador +1
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