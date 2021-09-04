from Abstractas.Objeto import Objeto

class Primitivo(Objeto):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor=valor

    def toString(self):
        return str(self.valor)

    def getEntero(self):
        return int(self.valor)
    
    def getFloat(self):
        return float(self.valor)
    
    def getBoolean(self):
        if self.valor == "false":
            return False
        elif self.valor == "true":
            return True
    def getValue(self):
        return self.valor