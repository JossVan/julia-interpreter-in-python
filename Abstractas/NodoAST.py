from abc import ABC, abstractmethod

class NodoAST(ABC):
    def __init__(self, fila, columna):
        self.fila=fila
        self.columna=columna
        super().__init__()

    @abstractmethod
    def ejecutar(self,tree, table):
        pass

    @abstractmethod
    def getNodo(self):
        pass