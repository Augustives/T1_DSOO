from abc import ABC, abstractmethod


class AbstractControladorPessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_pessoa(self):
