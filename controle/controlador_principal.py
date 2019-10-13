from limite.tela_inicial import TelaInicial
from controle.controlador_pessoa import ControladorPessoa
from controle.abstract_controlador_principal import AbstractControladorPrincipal


class ControladorPrincipal(AbstractControladorPrincipal):
    def __init__(self):
        super().__init__()
        self.__tela_inicial = TelaInicial(self)

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        escolhas = {1: self.vai_controlador_pessoa,
                    2: self.vai_controlador_quadra,
                    3: self.vai_controlador_aluguel}

        escolha = self.__tela_inicial.mostra_opcoes()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()

    @staticmethod
    def vai_controlador_pessoa():
        ControladorPessoa.inicia()

    @staticmethod
    def vai_controlador_quadra():
        pass

    @staticmethod
    def vai_controlador_aluguel():
        pass



