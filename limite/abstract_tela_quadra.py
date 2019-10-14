from abc import ABC, abstractmethod


class AbstractTelaQuadra(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    @abstractmethod
    def tela_add_quadra(self):
        pass

    @abstractmethod
    def tela_remove_quadra(self):
        pass

    @abstractmethod
    def tela_edit_quadra(self):
        pass

    @abstractmethod
    def tela_listar_quadras(self):
        pass

    def tela_listar_quadras_esporte(self, esporte):
        pass
