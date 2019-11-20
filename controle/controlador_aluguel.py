from controle.abstract_controlador_aluguel import AbstractControladorAluguel
from entidade.aluguel import Aluguel
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException


class ControladorAluguel(AbstractControladorAluguel):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_aluguel import TelaAluguel
        super().__init__()
        self.__lista_alugueis = list()
        self.__lista_nomes = list()
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
        try:
            quadra_escolhida = self.__controlador_principal.encontra_quadra(quadra[2])
            pessoa_escolhida = self.__controlador_principal.encontra_pessoa(nome_usuario)
            if quadra_escolhida is None or pessoa_escolhida is None:
                raise ValueError
            for aluguel in self.__lista_alugueis:
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
        self.__lista_alugueis.append(aluguel_marcado)
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
        print(confirmacao)
        if confirmacao == 1:
            quadra_alugada = self.__controlador_principal.encontra_quadra(info[2])
            for aluguel in self.__lista_alugueis:
                if (aluguel.quadra == quadra_alugada and
                        aluguel.dia == info[4] and aluguel.mes == info[6]
                        and aluguel.hora == info[8]):
                    self.__lista_alugueis.remove(aluguel)
                    self.__lista_nomes.remove([info[0], info[1], info[2], '-->',
                                               info[4], '/', info[6], '-', info[8]])
                    print("Aluguel cancelado com sucesso.")
                    self.abre_tela_aluguel()
            print("Aluguel inexistente.")
            self.abre_tela_aluguel()
        else:
            self.abre_tela_aluguel()


    def lista_aluguel_dia(self):
        dia = self.__tela_aluguel.tela_lista_aluguel_dia()
        for aluguel in self.__lista_alugueis:
            if aluguel.dia == dia:
                print("-"*30)
                print(aluguel.pessoa.nome)
                print(aluguel.pessoa.cpf)
                print(aluguel.quadra.identificador)
                print(aluguel.dia, "/", aluguel.mes, "às",
                      aluguel.hora, "horas")

    def voltar(self):
        self.__controlador_principal.inicia()

    def recibo(self, info_alguel):
        self.abre_tela_aluguel()

    @property
    def lista_nomes(self):
        return self.__lista_nomes
