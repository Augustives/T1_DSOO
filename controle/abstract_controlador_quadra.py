from abc import ABC, abstractmethod


class AbstractControladorQuadra(ABC):
    @abstractmethod
    def __init__(self):
        self.__lista_quadras = []
        pass

    @abstractmethod
    def add_quadra(self,  esporte: str, tipo: str, identificador: int):
        pass

    @abstractmethod
    def remove_quadra(self, identificador):
        pass

    @abstractmethod
    def edit_quadra(self):
        pass

    @abstractmethod
    def lista_quadras(self):
        pass

    @abstractmethod
    def lista_quadras_tipo(self, tipo):
        pass

    @abstractmethod
    def lista_quadras_esporte(self, esporte):
        pass

    @abstractmethod
    def abre_tela_quadras(self):
        pass
