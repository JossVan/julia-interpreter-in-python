class Simbolo:

    def __init__(self, identificador, valor, ambito, fila, columna, tipo):
        self.identificador = identificador
        self.valor = valor
        self.ambito = ambito
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
    
    def getTipo(self):
        return self.tipo
        
    def getID(self):
        return self.identificador.lower()
    
    def getValor(self):
        return self.valor
    
    def setValor(self,valor):
        self.valor = valor
        
    def getAmbito(self):
        return self.ambito

    def getFila(self):
        return self.fila 
    
    def getColumna(self):
        return self.columna