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
        pass

    @property
    @abstractmethod
    def quadra(self):
        pass

    @property
    @abstractmethod
    def data_str(self):
        pass

    @property
    @abstractmethod
    def data_date(self):
        pass