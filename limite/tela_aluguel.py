from limite.abstract_tela import AbstractTela


class TelaAluguel(AbstractTela):
    from controle.controlador_aluguel import ControladorAluguel

    def __init__(self, controlador: ControladorAluguel):
        super().__init__()
        self.__controlador = controlador

    def mostra_opcoes(self):
        print("---------- CADASTRO ALUGUÉIS----------")
        print("1 - Adicionar um aluguel.")
        print("2 - Remover um aluguel.")
        print("3 - Listar alugueis no mes.")
        print("4 - Listar alugueis por dia.")
        print("5 - ")
        print("0 - Voltar")
        print("-----------------------------------------")

        escolha = self.le_num_inteiro("Escolha uma das opções:",
                                      [1, 2, 3, 4, 5, 0])
        return escolha

    @staticmethod
    def tela_add_aluguel():
        print("Você escolheu cadastrar um novo aluguel. \n"
              "Informe os dados necessarios, por favor.")
        while True:
            try:
                identificador = int(input("Identificador da quadra: "))
                cpf = str(input("CPF: "))
                dia = int(input("Dia: "))
                mes = int(input("Mes: "))
                hora = int(input("Hora: "))
                if (identificador <= 0 or not (0 >= dia > 31) or
                        len(cpf) != 11 or not cpf.isdigit() or not (0 >= mes > 12) or not(0 > hora > 24)):
                    raise ValueError
                return identificador, cpf, dia, mes, hora
            except ValueError:
                print("Dados oferecidos inválidos. "
                      "Preencha novamente, por favor.")

    @staticmethod
    def tela_remove_aluguel():
        print("Você escolheu excluir um aluguel. "
              "Informe o Identificador da quadra, o dia, o mes e o horario, por favor.")
        while True:
            try:
                identificador = int(input("Identificador da Quadra: "))
                dia = int(input("Dia: "))
                mes = int(input("Mes: "))
                hora = int(input("Hora: "))
                if (identificador <= 0 or not (dia <= 0 and dia > 31)
                        or not (mes <= 0 and mes > 12) or not (hora < 0 and hora > 24):
                    raise ValueError
                return identificador, dia, mes, hora
            except ValueError:
                print("Informacoes invalidas. preencha novamente, por favor.")


    def tela_lista_aluguel_mes():



