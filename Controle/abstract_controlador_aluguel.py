from abc import ABC, abstractmethod


class AbstractControladorAluguel(ABC):
    @abstractmethod
    def __init__(self):
        self.__dict_aluguel = {}
        pass
#Lista de dicionarios separados por mes ?

    @abstractmethod
    def add_aluguel(self):
        pass

    @abstractmethod
    def remove_aluguel(self):
        pass

    @abstractmethod
    def lista_aluguel_mes(self):
        pass

    @abstractmethod
    def lista_quadras_disponiveis_dia(self):
        pass

    @abstractmethod
    def lista_aluguel_data(self):
        pass

    @abstractmethod
    def lista_aluguel_pessoa(self):
        pass

    @abstractmethod
    def quadra_mais_alugada(self):
        pass

    @abstractmethod
    def abre_tela_aluguel(self):
        pass
