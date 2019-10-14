from limite.abstract_tela import AbstractTela


class TelaAluguel(AbstractTela):
    from controle.controlador_aluguel import ControladorAluguel

    def __init__(self, controlador: ControladorAluguel):
        super().__init__()
        self.__controlador = controlador

    def mostra_opcoes(self):
        print("---------- CADASTRO ALUGUÉIS----------")
        print("1 - Adicionar um aluguel.")
        print("2 - ")
        print("3 - ")
        print("4 - ")
        print("5 - ")
        print("0 - Voltar")
        print("-----------------------------------------")

        escolha = self.le_num_inteiro("Escolha uma das opções:",
                                      [1, 2, 3, 4, 5, 0])
        return escolha

    def tela_add_aluguel(self):
        pass

    def tela_remove_aluguel(self):
        pass

    def tela_lista_aluguel_mes(self):
        pass

