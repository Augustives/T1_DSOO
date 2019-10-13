from abc import ABC, abstractmethod


class AbstractTelaPessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    @abstractmethod
    def cadastra_pessoa(self):
        pass

    @abstractmethod
    def remove_pessoa(self):
        pass

    @abstractmethod
    def altera_pessoa(self):
        pass

    @abstractmethod
    def mostra_pessoa(self):
        pass
