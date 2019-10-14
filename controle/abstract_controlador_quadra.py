from abc import ABC, abstractmethod


class AbstractControladorQuadra(ABC):
    @abstractmethod
    def __init__(self):
        self.__lista_quadras = []
        pass

    @abstractmethod
    def inicia(self):
        pass

    @abstractmethod
    def add_quadra(self):
        pass

    @abstractmethod
    def remove_quadra(self):
        pass

    @abstractmethod
    def edit_quadra(self):
        pass

    @property
    @abstractmethod
    def lista_quadras(self):
        pass

    @abstractmethod
    def listar_quadras(self):
        pass

    @abstractmethod
    def listar_quadras_esporte(self):
        pass

    @abstractmethod
    def abre_tela_quadra(self):
        pass

    @abstractmethod
    def voltar(self):
        pass

    @abstractmethod
    def encontra_quadra(self, identificador):
        pass
