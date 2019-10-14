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

    def tela_add_aluguel(self):
        print("Você escolheu cadastrar um novo aluguel. \n"
              "Informe os dados necessarios, por favor.")
        while True:
            try:
                identificador = int(input("Identificador da quadra: "))
                cpf = str(input("CPF: "))
                dia = int(input("Dia: "))
                mes = int(input("Mes: "))
                hora = int(input("Hora: "))
                if (identificador <= 0 or (dia<= 0 and dia > 31) or
                        len(cpf) != 11 or not cpf.isdigit() or (mes <=0 and mes > 12) or (hora < 0 and hora > 24):
                    raise ValueError
                return identificador, cpf, mes, dia, hora
            except ValueError:
                print("Dados oferecidos inválidos. "
                      "Preencha novamente, por favor.")

    def tela_remove_aluguel(self):
        pass

    def tela_lista_aluguel_mes(self):
        pass

