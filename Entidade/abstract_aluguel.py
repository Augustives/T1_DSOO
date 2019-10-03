from abc import ABC, abstractmethod
from datetime import date as Date

class AbstractAluguel(ABC):

    @abstractmethod
    def __init__(self, pessoa: Pessoa, quadra: Quadra, data_str: str):
    # https://stackabuse.com/converting-strings-to-datetime-in-python/
        self.__pessoa = pessoa
        self.__quadra = quadra
        self.__data_str = data_str


