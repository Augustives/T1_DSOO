from controle.abstract_controlador_quadra import AbstractControladorQuadra
from entidade.quadra import Quadra
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException
from controle.quadra_dao import QuadraDAO
from limite.tela_popup import Popup


class ControladorQuadra(AbstractControladorQuadra):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_quadra import TelaQuadra
        super().__init__()
        self.__quadras_DAO = QuadraDAO()
        self.__lista_nomes = list()
        self.__controlador_principal = controlador_principal
        for quadra in self.__quadras_DAO.get_all():
            lista = [quadra.esporte, quadra.tipo, quadra.identificador]
            self.__lista_nomes.append(lista)

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
        print(esporte, tipo, identificador)
        if esporte is None and tipo is None and identificador is None:
            self.abre_tela_quadra()
        try:
            if esporte == "" or tipo == "" or int(identificador) <= 0:
                raise ValueError
            for quadra in self.__quadras_DAO.get_all():
                if quadra.identificador == identificador:
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Quadra já cadastrada.")
            Popup('Quadra já cadastrada.')
            self.abre_tela_quadra()
        except ValueError:
            print('Valores Inválidos.')
            Popup('Valores Inválidos.')
            self.abre_tela_quadra()

        quadra_nova = Quadra(esporte, tipo, identificador)
        self.__quadras_DAO.add(quadra_nova)
        self.__lista_nomes.append([quadra_nova.esporte, quadra_nova.tipo,
                                  quadra_nova.identificador])
        print("Quadra cadastrada com sucesso.")
        Popup("Quadra cadastrada com sucesso.")
        self.abre_tela_quadra()

    def remove_quadra(self, info_quadra: list):
        info = info_quadra
        from limite.tela_remove_quadra import TelaRemoveQuadra
        tela_confirmacao = TelaRemoveQuadra('Remover Quadra',
                                            'Você tem certeza que deseja \n '
                                            'excluir esse cadastro?')
        confirmacao = tela_confirmacao.mostra_opcoes()
        if confirmacao == 1:
            for quadra in self.__quadras_DAO.get_all():
                if quadra.identificador == info[2]:
                    self.__quadras_DAO.remove(info[2])
                    self.__lista_nomes.remove([quadra.esporte, quadra.tipo,
                                               quadra.identificador])
                    for i in range(len(self.__lista_nomes)):
                        if self.__lista_nomes[i][2] == info[2]:
                            self.__lista_nomes.pop(i)

                    print("Quadra removida com sucesso.")
                    Popup('Quadra removida com sucesso')
                    self.abre_tela_quadra()
            print("Quadra inexistente.")
            Popup('Quadra inexistente')
            self.abre_tela_quadra()
        else:
            self.abre_tela_quadra()

    def edit_quadra(self, info_quadra: list):
        from limite.tela_add_edit_quadra import TelaAddEditQuadra
        tela_edit_quadra = TelaAddEditQuadra('Editar Quadra',
                                             ['Esporte', 'Tipo', 'Identificador'],
                                             'Alterar Informações')
        esporte, tipo, identificador = tela_edit_quadra.mostra_opcoes()
        if esporte is None and tipo is None and identificador is None:
            self.abre_tela_quadra()
        for quadra in self.__quadras_DAO.get_all():
            if str(quadra.identificador) == str(info_quadra[2]):
                info_antiga = [quadra.esporte, quadra.tipo, quadra.identificador]
                quadra_antiga = quadra
                if esporte != "":
                    quadra.esporte = esporte
                if tipo != "":
                    quadra.tipo = tipo
                if identificador != "":
                    quadra.identificador = identificador
                quadra_alterada = quadra
                self.__lista_nomes[self.__lista_nomes.index(info_antiga)] \
                    = [quadra.esporte, quadra.tipo, quadra.identificador]
                self.__quadras_DAO.edit(quadra_antiga, quadra_alterada)
                self.abre_tela_quadra()
        print("Quadra inexistente.")
        Popup('Quadra inexistente.')
        self.abre_tela_quadra()

    @property
    def lista_quadras(self):
        return self.__quadras_DAO.get_all()

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
        return self.__quadras_DAO.get(identificador)
