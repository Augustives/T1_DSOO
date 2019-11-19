from controle.abstract_controlador_quadra import AbstractControladorQuadra
from entidade.quadra import Quadra
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException


class ControladorQuadra(AbstractControladorQuadra):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_quadra import TelaQuadra
        super().__init__()
        self.__controlador_principal = controlador_principal
        self.__lista_quadras = list()
        self.__lista_nomes = list()
        self.__tela_quadra = TelaQuadra(self, 'Tela Quadra', ['Cadastrar Quadra', 'Excluir Quadra',
                                                              'Editar Quadra', 'Voltar'],
                                        self.__lista_nomes)

    def inicia(self):
        self.abre_tela_quadra()

    def add_quadra(self):
        from limite.tela_add_edit_quadra import TelaAddEditQuadra
        tela_add_quadra = TelaAddEditQuadra('Cadastrar Quadra',
                                            ['Esporte', 'Tipo', 'Identificador'],
                                            'Cadastrar')
        esporte, tipo, identificador = tela_add_quadra.mostra_opcoes()

        try:
            if esporte == "" or tipo == "" or int(identificador) <= 0:
                raise ValueError
            for quadra in self.__lista_quadras:
                if quadra.identificador == identificador:
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Quadra já cadastrada.")
            self.abre_tela_quadra()
        except ValueError:
            print('Valores Inválidos.')
            self.abre_tela_quadra()

        quadra_nova = Quadra(esporte, tipo, identificador)
        self.__lista_quadras.append(quadra_nova)
        self.__lista_nomes.append([quadra_nova.esporte, quadra_nova.tipo,
                                  quadra_nova.identificador])
        print("Quadra cadastrada com sucesso.")
        self.abre_tela_quadra()

    def remove_quadra(self, info_quadra: list):
        info = info_quadra
        from limite.tela_remove_quadra import TelaRemoveQuadra
        tela_confirmacao = TelaRemoveQuadra('Remover Quadra',
                                            'Você tem certeza que deseja \n '
                                            'excluir esse cadastro?')
        confirmacao = tela_confirmacao.mostra_opcoes()
        if confirmacao == 1:
            for quadra in self.__lista_quadras:
                if quadra.identificador == info[2]:
                    self.__lista_quadras.remove(quadra)
                    self.__lista_nomes.remove([quadra.esporte, quadra.tipo,
                                               quadra.identificador])
                    print("Quadra removida com sucesso.")
                    self.abre_tela_quadra()
            print("Quadra inexistente.")
            self.abre_tela_quadra()
        else:
            self.abre_tela_quadra()

    def edit_quadra(self, info_quadra: list):
        from limite.tela_add_edit_quadra import TelaAddEditQuadra
        tela_edit_quadra = TelaAddEditQuadra('Editar Quadra',
                                             ['Esporte', 'Tipo', 'Identificador'],
                                             'Alterar Informações')
        esporte, tipo, identificador = tela_edit_quadra.mostra_opcoes()
        for quadra in self.__lista_quadras:
            if quadra.identificador == info_quadra[2]:
                info_antiga = [quadra.esporte, quadra.tipo, quadra.identificador]
                if esporte != "":
                    quadra.esporte = esporte
                if tipo != "":
                    quadra.tipo = tipo
                if identificador != "":
                    quadra.identificador = identificador
                self.__lista_nomes[self.__lista_nomes.index(info_antiga)] \
                    = [quadra.esporte, quadra.tipo, quadra.identificador]
                self.abre_tela_quadra()
        print("Quadra inexistente.")
        self.abre_tela_quadra()

    @property
    def lista_quadras(self):
        return self.__lista_quadras

    @property
    def lista_nomes(self):
        return self.__lista_nomes

    def voltar(self):
        self.__controlador_principal.inicia()

    def abre_tela_quadra(self):
        escolhas = {1: self.add_quadra, 2: self.remove_quadra,
                    3: self.edit_quadra, 4: self.voltar}
        escolha, quadra = self.__tela_quadra.mostra_opcoes()
        if escolha is None:
            escolha = 4
        funcao_escolhida = escolhas[escolha]
        if escolha in [1, 4]:
            funcao_escolhida()
        else:
            try:
                funcao_escolhida(quadra[0][0])
            except IndexError:
                self.abre_tela_quadra()

    def encontra_quadra(self, identificador):
        for quadra in self.__lista_quadras:
            if quadra.identificador == identificador:
                return quadra
