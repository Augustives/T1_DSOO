from controle.controlador_aluguel import ControladorAluguel
from controle.abstract_controlador_principal import AbstractControladorPrincipal


class ControladorPrincipal(AbstractControladorPrincipal):
    def __init__(self):
        from limite.tela_inicial import TelaInicial
        from controle.controlador_pessoa import ControladorPessoa
        from controle.controlador_quadra import ControladorQuadra
        super().__init__()
        self.__tela_inicial = TelaInicial(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_quadra = ControladorQuadra(self)

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        escolhas = {1: self.vai_controlador_pessoa,
                    2: self.vai_controlador_quadra,
                    3: self.vai_controlador_aluguel}

        escolha = self.__tela_inicial.mostra_opcoes()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()

    def vai_controlador_pessoa(self):
        self.__controlador_pessoa.inicia()

    def vai_controlador_quadra(self):
        self.__controlador_quadra.inicia()

    @staticmethod
    def vai_controlador_aluguel():
        ControladorAluguel().inicia()




