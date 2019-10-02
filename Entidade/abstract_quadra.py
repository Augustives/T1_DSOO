from abc import ABC, abstractmethod

class AbstractQuadra(ABC):

    @abstractmethod
    def __init__(self, esporte: str, tipo: str, identificador: int):
        self.__esporte = esporte
        self.__tipo = tipo
        self.__identificador = identificador
        pass


    @property
    @abstractmethod
    def esporte(self):
        return self.__esporte


    @esporte.setter
    @abstractmethod
    def esporte(self, esporte):
        self.__esporte = esporte


    @property
    @abstractmethod
    def tipo(self):
        return self.__tipo


    @tipo.setter
    @abstractmethod
    def tipo(self, tipo):
        self.__tipo = tipo


    @property
    @abstractmethod
    def identificador(self):
        return self.__identificador


    @identificador.setter
    @abstractmethod
    def identificador(self, identificador):
        self.__identificador = identificador
