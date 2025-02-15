from abc import ABC, abstractmethod


class AbstractQuadra(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def esporte(self):
        pass

    @esporte.setter
    @abstractmethod
    def esporte(self, esporte):
        pass

    @property
    @abstractmethod
    def tipo(self):
        pass

    @tipo.setter
    @abstractmethod
    def tipo(self, tipo):
        pass

    @property
    @abstractmethod
    def identificador(self):
        pass

    @identificador.setter
    @abstractmethod
    def identificador(self, identificador):
        pass
