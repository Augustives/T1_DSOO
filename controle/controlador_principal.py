from controle.abstract_controlador_principal import AbstractControladorPrincipal
import sys


class ControladorPrincipal(AbstractControladorPrincipal):
    def __init__(self):
        from limite.tela_inicial import TelaInicial
        from controle.controlador_pessoa import ControladorPessoa
        from controle.controlador_quadra import ControladorQuadra
        from controle.controlador_aluguel import ControladorAluguel
        super().__init__()
        self.__tela_inicial = TelaInicial(self, 'Tela Inicial', ['Pessoas',
                                                                 'Quadras',
                                                                 'Aluguéis'])
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_quadra = ControladorQuadra(self)
        self.__controlador_aluguel = ControladorAluguel(self)

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        escolhas = {1: self.vai_controlador_pessoa,
                    2: self.vai_controlador_quadra,
                    3: self.vai_controlador_aluguel}

        escolha = self.__tela_inicial.mostra_opcoes()
        if escolha is None:
            sys.exit()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()

    def vai_controlador_pessoa(self):
        self.__controlador_pessoa.inicia()

    def vai_controlador_quadra(self):
        self.__controlador_quadra.inicia()

    def vai_controlador_aluguel(self):
        self.__controlador_aluguel.inicia()

    def encontra_pessoa(self, nome):
        return self.__controlador_pessoa.encontra_pessoa(nome)

    def encontra_quadra(self, identificador):
        return self.__controlador_quadra.encontra_quadra(identificador)

    def lista_nomes_pessoas(self):
        return self.__controlador_pessoa.lista_nomes

    def lista_info_quadras(self):
        return self.__controlador_quadra.lista_nomes

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
