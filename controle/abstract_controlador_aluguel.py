from abc import ABC, abstractmethod


class AbstractControladorAluguel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inicia(self):
        pass

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
    def lista_aluguel_dia(self):
        pass

    @abstractmethod
    def abre_tela_aluguel(self):
        pass

    @abstractmethod
    def recibo(self, nome: str, cpf: str,
               esporte: str, dia: int,
               mes: int, horario: int):
        pass

    @abstractmethod
    def voltar(self):
        pass
