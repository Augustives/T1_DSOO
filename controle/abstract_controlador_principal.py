from abc import ABC, abstractmethod


class AbstractControladorPrincipal(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def abre_tela_inicial(self):
        pass

    @abstractmethod
    def inicia(self):
        pass

    @abstractmethod
    def vai_controlador_pessoa(self):
        pass

    @abstractmethod
    def vai_controlador_quadra(self):
        pass

    @abstractmethod
    def vai_controlador_aluguel(self):
        pass
