from entidade.abstract_aluguel import AbstractAluguel
from entidade.quadra import Quadra
from entidade.pessoa import Pessoa


class Aluguel(AbstractAluguel):
    def __init__(self, pessoa: Pessoa, quadra: Quadra, dia: str, mes: str, hora: str):
        super().__init__()
        self.__pessoa = pessoa
        self.__quadra = quadra
        self.__dia = dia
        self.__mes = mes
        self.__hora = hora

    @property
    def pessoa(self):
        return self.__pessoa

    @property
    def quadra(self):
        return self.__quadra

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def hora(self):
        return self.__hora
