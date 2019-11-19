from abc import ABC, abstractmethod


class AbstractControladorPessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inicia(self):
        pass

    @abstractmethod
    def add_pessoa(self):
        pass

    @abstractmethod
    def remove_pessoa(self, nome: str):
        pass

    @abstractmethod
    def edit_pessoa(self, nome: str):
        pass

    @abstractmethod
    def dados_pessoa(self, nome: str):
        pass

    @abstractmethod
    def lista_pessoas(self):
        pass

    @abstractmethod
    def voltar(self):
        pass

    @abstractmethod
    def abre_tela_pessoa(self):
        pass

    @abstractmethod
    def encontra_pessoa(self, cpf):
        pass
