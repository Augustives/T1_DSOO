from abc import ABC, abstractmethod

class AbstractTelaAluguel():
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    @abstractmethod
    def cadastra_aluguel(self):
        pass

    @abstractmethod
    def retira_aluguel(self):
        pass

    @abstractmethod
    def quadras_disponiveis(self):
        pass

    @abstractmethod
    def mostra_opcoes_lista(self):
        pass

    @abstractmethod
    def aluguel_pessoa(self):
        pass

    @abstractmethod
    def aluguel_mes(self):
        pass

    @abstractmethod
    def aluguel_dia(self):
        pass

    @abstractmethod
    def quadra_mais_alugada(self):
        pass

