from abc import ABC, abstractmethod


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
    def dia(self):
        pass

    @property
    @abstractmethod
    def mes(self):
        pass

    @property
    @abstractmethod
    def hora(self):
        pass
