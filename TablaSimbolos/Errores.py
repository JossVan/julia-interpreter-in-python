from Abstractas.Objeto import TipoObjeto

class Errores:

    def __init__(self, error, tipo, descripcion, fila, columna):
        self.error=error
        self.tipo = tipo 
        self.descripcion = descripcion
        self.fila = fila 
        self.columna = columna 
    
    def getCadena(self):
        cadena ="Error en "+ str(self.error) + ", "+ str(self.descripcion)+", fila "+ str(self.fila)+ ", columna "+str(self.columna)
        return cadena
    