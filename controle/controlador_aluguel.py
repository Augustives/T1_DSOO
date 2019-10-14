from controle.abstract_controlador_aluguel import AbstractControladorAluguel
from entidade.aluguel import Aluguel
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException
from datetime import datetime


class ControladorAluguel(AbstractControladorAluguel):
    def __init__(self):
        from limite.tela_aluguel import TelaAluguel
        super().__init__()
        self.__tela_aluguel = TelaAluguel(self)
        self.__lista_alugueis = list()

    def inicia(self):
        self.abre_tela_aluguel()

    def abre_tela_aluguel(self):
        escolhas = {}  # precisa colocar as escolhas
        escolha = self.__tela_aluguel.mostra_opcoes()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()

    # não tá perfeito ainda
    def add_aluguel(self):
        pessoa, quadra, data_str = self.__tela_aluguel.tela_add_aluguel()
        data_date = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        try:
            for aluguel in self.__lista_alugueis:
                if (aluguel.quadra == quadra and
                   aluguel.data_horario == data_date):
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Quadra indisponível no horário desejado.")
            self.abre_tela_aluguel()

        aluguel_marcado = Aluguel(pessoa, quadra, data_str)
        self.__lista_alugueis.append(aluguel_marcado)
        print("Usuário cadastrado com sucesso.")
        self.abre_tela_aluguel()

    def remove_aluguel(self):
        quadra, data_str = self.__tela_aluguel.tela_remove_aluguel()
        data_date = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        for aluguel in self.__lista_alugueis:
            if (aluguel.quadra == quadra and
                    aluguel.data_horario == data_date):
                self.__lista_alugueis.remove(aluguel)
                print("Aluguel cancelado com sucesso.")
                self.abre_tela_aluguel()
        print("Aluguel inexistente.")
        self.abre_tela_aluguel()

    def lista_aluguel_mes(self):
        mes = self.__tela_aluguel.tela_lista_aluguel_mes()
        for aluguel in self.__lista_alugueis:
            if aluguel.data_horario.month == mes:
                print("-"*30)
                print(aluguel.pessoa)
                print(aluguel.quadra)
                print(aluguel.data_horario)

    def lista_aluguel_pessoa(self):
        pass





