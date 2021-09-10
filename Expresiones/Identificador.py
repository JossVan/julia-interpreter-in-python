from Abstractas.NodoArbol import NodoArbol
from TablaSimbolos.Errores import Errores
from Abstractas.NodoAST import NodoAST

class Identificador(NodoAST):

    def __init__(self, id, fila, columna):
        self.id = id 
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        
        self.id = self.id.lower()
        resultado = table.BuscarIdentificador(self.id)
        if resultado == None:
            tree.insertError(Errores("Variable no encontrada","Semántico","No definida", self.fila,self.columna))
            return "No existe la variable"
        return resultado.getValor()
    
    def getNodo(self):
        NuevoNodo = NodoArbol("ID")
        NuevoNodo.agregarHijo(self.id)
        