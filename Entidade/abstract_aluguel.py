from abc import ABC, abstractmethod
# https://stackabuse.com/converting-strings-to-datetime-in-python/

class AbstractAluguel(ABC):

    @abstractmethod
    def __init__(self, pessoa, quadra, data_str: str):
        self.__pessoa = pessoa
        self.__quadra = quadra
        self.__data_str = data_str
        self.__data_date = datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M')
        pass

    @property
    @abstractmethod
    def pessoa(self):
        return self.__pessoa

    @property
    @abstractmethod
    def quadra(self):
        return self__quadra

    @property
    @abstractmethod
    def data_str(self):
        return self__data_str

    @property
    @abstractmethod
    def data_date(self):
        return self.__data_date