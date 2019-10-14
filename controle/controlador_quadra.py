from Controle.abstract_controlador_quadra import AbstractControladorQuadra
from Entidade.quadra import Quadra

class ControladorQuadra(AbstractControladorQuadra):
    def __init__(self):
        from Limite.tela_quadra import TelaQuadra
        super().__init__()
        self.__tela_quadra = TelaQuadra(self)
        self.__lista_quadras = []
        self.__identificador = 0
        self.__lista_identificador = []

    @property
    def lista_identificador(self):
        return self.__lista_identificador

    def inicia(self):
        self.abre_tela_quadra()

    def add_quadra(self):
        esporte, tipo = self.__tela_quadra.tela_add_quadra()
        self.__identificador += 1
        self.__lista_identificador.append(self.__identificador)
        identificador = self.__identificador
        identificador = Quadra(esporte, tipo, identificador)
        self.__lista_quadras.append(identificador)
        print("Usuário cadastrado com sucesso.")
        self.abre_tela_quadra()

    def remove_quadra(self):
        identificador = self.__tela_quadra.tela_remove_quadra()
        if identificador in self.__lista_quadras:
            self.lista_quadras().remove(identificador)


    def edit_quadra(self):
        esporte, tipo, identificador = self.__tela_quadra.tela_edit_quadra()
        for quadra in self.__lista_quadras:
            if quadra.identificador == identificador:
                if esporte != "":
                    quadra.esporte = esporte
                if tipo != "":
                    quadra.tipo = tipo
                print("INFORMAÇÕES ATUALIZADAS:\n "
                      "Esporte: {}\n "
                      "Tipo: {}"
                      "Identificador: {}".format(quadra.esporte, quadra.tipo,
                                         quadra.identificador))
                self.abre_tela_quadra()
        print("Quadra inexistente.")
        self.abre_tela_quadra()

    @property
    def lista_quadras(self):
        return self.__lista_quadras

    def listar_quadras(self):
        self.__tela_quadra.tela_listar_quadras()
        self.abre_tela_quadra()

    @staticmethod
    def voltar():
        from Controle.controlador_principal import ControladorPrincipal
        ControladorPrincipal().inicia()

    def abre_tela_quadra(self):
        escolhas = {1: self.add_quadra, 2: self.remove_quadra,
                    3: self.edit_quadra, 4: self.listar_quadras,
                    5: self.listar_quadras, 0: self.voltar}
        escolha = self.__tela_quadra.mostra_opcoes()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()
