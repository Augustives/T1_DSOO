from abc import ABC, abstractmethod
# https://stackabuse.com/converting-strings-to-datetime-in-python/


class AbstractAluguel(ABC):
    @abstractmethod
    def __init__(self):
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
