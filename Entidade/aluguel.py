from Entidade.abstract_aluguel import AbstractAluguel
from Entidade.quadra import Quadra
from Entidade.pessoa import Pessoa
from datetime import datetime

class Aluguel(AbstractAluguel):

    def __init__(self, pessoa: Pessoa, quadra: Quadra, data_str: str):
        super().__init__(pessoa: Pessoa, quadra: Quadra, data_str: str)
        self.__pessoa = pessoa
        self.__quadra = quadra
        self.__data_str = data_str
        self.__data_date = datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M')

    @property
    def pessoa(self):
        return self.__pessoa

    @property
    def quadra(self):
        return self__quadra

    @property
    def data_str(self):
        return self__data_str

    @property
    def data_date(self):
        return self.__data_date
