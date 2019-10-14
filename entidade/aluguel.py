from Entidade.abstract_aluguel import AbstractAluguel
from Entidade.quadra import Quadra
from Entidade.pessoa import Pessoa
from datetime import datetime


class Aluguel(AbstractAluguel):
    def __init__(self, pessoa: Pessoa, quadra: Quadra, data_str: str):
        super().__init__()
        self.__pessoa = pessoa
        self.__quadra = quadra
        self.__data_horario = datetime.strptime(data_str, '%d/%m/%Y %H:%M')

    @property
    def pessoa(self):
        return self.__pessoa

    @property
    def quadra(self):
        return self.__quadra

    @property
    def data_horario(self):
        return self.__data_horario
