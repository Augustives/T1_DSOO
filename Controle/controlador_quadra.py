from Controle.abstract_controlador_quadra import AbstractControladorQuadra
from Entidade.quadra import Quadra

class ControladorQuadra(AbstractControladorQuadra):
    def __init__(self):
        super().__init__()
        self.__lista_quadras = []

    def add_quadra(self,  esporte: str, tipo: str, identificador: int):
        identificador = Quadra(esporte, tipo, identificador)
        self.__lista_quadras.append(identificador)

    def remove_quadra(self, identificador):
        if identificador in self.__lista_quadras:
            self.lista_quadras().remove(identificador)


