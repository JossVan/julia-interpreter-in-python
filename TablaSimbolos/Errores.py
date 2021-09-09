from Abstractas.Objeto import TipoObjeto

class Errores:

    def __init__(self, error, tipo, descripcion, fila, columna):
        self.error=error
        self.tipo = tipo 
        self.descripcion = descripcion
        self.fila = fila 
        self.columna = columna 
        self.tipo = TipoObjeto.ERROR
    
    def getCadena(self):
        return "Error en "+ self.error + ", "+ self.descripcion+", fila "+self.fila+", columna "+self.columna
    
    