from entidade.abstract_quadra import AbstractQuadra

class Quadra(AbstractQuadra):
    def __init__(self, esporte: str, tipo: str, identificador: int):
        super().__init__(esporte: str, tipo: str, identificador: int)
        self.__esporte = esporte
        self.__tipo = tipo
        self.__identificador = identificador

    @property
    def esporte(self):
        return self.__esporte


    @esporte.setter
    def esporte(self, esporte):
        self.__esporte = esporte


    @property
    def tipo(self):
        return self.__tipo


    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo


    @property
    def identificador(self):
        return self.__identificador


    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

