from controle.abstract_controlador_aluguel import AbstractControladorAluguel
from entidade.aluguel import Aluguel
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException
from controle.aluguel_dao import AlugelDAO


class ControladorAluguel(AbstractControladorAluguel):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_aluguel import TelaAluguel
        super().__init__()
        self.__aluguel_DAO = AlugelDAO()
        self.__lista_nomes = list()
        for aluguel in self.__aluguel_DAO.get_all():
            lista = [aluguel.quadra.esporte, aluguel.quadra.tipo,
                     aluguel.quadra.identificador, '-->',
                     aluguel.dia, '/', aluguel.mes, '-', aluguel.hora]
            self.__lista_nomes.append(lista)
        self.__tela_aluguel = TelaAluguel(self, 'Tela Aluguel',
                                          ['Novo Aluguel', 'Remover Aluguel',
                                           'Listar Aluguéis de Determinado Dia',
                                           'Gerar Recibo', 'Voltar'],
                                          self.__lista_nomes)
        self.__controlador_principal = controlador_principal

    def inicia(self):
        self.abre_tela_aluguel()

    def abre_tela_aluguel(self):
        escolhas = {1: self.add_aluguel, 2: self.remove_aluguel,
                    3: self.lista_aluguel_dia, 4: self.recibo, 5: self.voltar}
        escolha, aluguel = self.__tela_aluguel.mostra_opcoes()
        if escolha is None:
            escolha = 5
        funcao_escolhida = escolhas[escolha]
        if escolha in [1, 3, 5]:
            funcao_escolhida()
        else:
            try:
                funcao_escolhida(aluguel[0])
            except IndexError:
                self.abre_tela_aluguel()

    def add_aluguel(self):
        from limite.tela_add_aluguel import TelaAddAluguel
        tela_add_aluguel = TelaAddAluguel('Cadastrar Aluguel',
                                          self.__controlador_principal.lista_nomes_pessoas(),
                                          self.__controlador_principal.lista_info_quadras())
        nome_usuario, quadra, mes, dia, hora = tela_add_aluguel.mostra_opcoes()
        print(nome_usuario, quadra, mes, dia, hora)
        if (nome_usuario is None and quadra is None
                and mes is None and dia is None and hora is None):
            self.abre_tela_aluguel()
        try:
            quadra_escolhida = self.__controlador_principal.encontra_quadra(quadra[2])
            pessoa_escolhida = self.__controlador_principal.encontra_pessoa(nome_usuario)
            print(quadra_escolhida)
            print(pessoa_escolhida)
            print(nome_usuario)
            if quadra_escolhida is None or pessoa_escolhida is None:
                raise ValueError
            for aluguel in self.__aluguel_DAO.get_all():
                if (aluguel.quadra == quadra_escolhida and
                        aluguel.dia == dia and
                        aluguel.mes == mes and aluguel.hora == hora):
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Aluguel indisponível no horário desejado.")
            self.abre_tela_aluguel()
        except ValueError:
            print("Quadra ou pessoa inexistentes.")
            self.abre_tela_aluguel()

        aluguel_marcado = Aluguel(self.__controlador_principal.encontra_pessoa(nome_usuario),
                                  self.__controlador_principal.encontra_quadra(quadra[2]),
                                  dia, mes, hora)
        self.__aluguel_DAO.add(aluguel_marcado)
        self.__lista_nomes.append([quadra[0], quadra[1], quadra[2], '-->',
                                   dia, '/', mes, '-', hora])
        print("Aluguel cadastrado com sucesso.")
        self.abre_tela_aluguel()

    def remove_aluguel(self, info_aluguel: list):
        info = info_aluguel[0]
        from limite.tela_remove_aluguel import TelaRemoveAluguel
        tela_confirmacao = TelaRemoveAluguel('Remover Aluguel',
                                             'Você tem certeza que deseja \n '
                                             'cancelar esse aluguel?')
        confirmacao = tela_confirmacao.mostra_opcoes()
        print(info)
        if confirmacao == 1:
            quadra_alugada = self.__controlador_principal.encontra_quadra(info[2])
            for aluguel in self.__aluguel_DAO.get_all():
                if (self.__controlador_principal.encontra_quadra(aluguel.quadra.identificador) == quadra_alugada and
                        aluguel.dia == info[4] and aluguel.mes == info[6]
                        and aluguel.hora == info[8]):
                    self.__aluguel_DAO.remove(aluguel)
                    self.__lista_nomes.remove([info[0], info[1], info[2], '-->',
                                               info[4], '/', info[6], '-', info[8]])
                    print("Aluguel cancelado com sucesso.")
                    self.abre_tela_aluguel()
            print("Aluguel inexistente.")
            self.abre_tela_aluguel()
        else:
            self.abre_tela_aluguel()

    def lista_aluguel_dia(self):
        from limite.tela_listar_por_dia import TelaListarPorDia
        tela = TelaListarPorDia('Tela escolher dia',
                                ['Dia desejado', 'Mês desejado'], 'Procurar')
        dia, mes = tela.mostra_opcoes()
        if dia is None and mes is None:
            self.abre_tela_aluguel()
        print(dia, mes)
        alugueis_no_dia = list()
        for aluguel in self.__aluguel_DAO.get_all():
            print(aluguel.dia, aluguel.mes)
            if str(aluguel.dia) == str(dia) and str(aluguel.mes) == str(mes):
                alugueis_no_dia.append([aluguel.quadra.esporte, aluguel.quadra.tipo,
                                        aluguel.quadra.identificador, '-->',
                                        aluguel.dia, '/', aluguel.mes, '-', aluguel.hora])

        from limite.tela_dados_listagem import TelaDadosListagem
        tela_dados_listagem = TelaDadosListagem('Aluguéis no dia {}/{}'.format(dia, mes),
                                                alugueis_no_dia)
        voltar = tela_dados_listagem.mostra_opcoes()
        if voltar == 1 or voltar is None:
            self.abre_tela_aluguel()

    def voltar(self):
        self.__controlador_principal.inicia()

    def recibo(self, info_alguel: list):
        info = info_alguel[0]
        print(info)
        from limite.tela_dados_aluguel import TelaDadosAluguel
        nome = None
        for aluguel in self.__aluguel_DAO.get_all():
            print(aluguel.pessoa)
            if (aluguel.quadra.esporte == info[0] and
                    aluguel.quadra.tipo == info[1] and
                    aluguel.quadra.identificador == info[2] and
                    aluguel.dia == info[4] and
                    aluguel.mes == info[6] and
                    aluguel.hora == info[8]):
                nome = aluguel.pessoa.nome

        tela_dados_aluguel = TelaDadosAluguel('Recibo de Aluguel',
                                              ['Quadra {} {} {}'.format(info[0], info[1], info[2]),
                                               'Alugada por ' + nome,
                                               'Na data {}/{} às {}.'.format(info[4], info[6], info[8])])
        voltar = tela_dados_aluguel.mostra_opcoes()
        if voltar == 1 or voltar is None:
            self.abre_tela_aluguel()

    @property
    def lista_nomes(self):
        return self.__lista_nomes
