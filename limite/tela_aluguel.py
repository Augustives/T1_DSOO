from limite.abstract_listagem import AbstractListagem


class TelaAluguel(AbstractListagem):
    from controle.controlador_aluguel import ControladorAluguel

    def __init__(self, controlador: ControladorAluguel,
                 nome_tela: str, texto_botoes: list, lista_alugueis: list):
        super().__init__(nome_tela, texto_botoes, lista_alugueis)
        self.__controlador = controlador

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
                if (identificador <= 0 or dia > 31 or dia < 1 or
                        len(cpf) != 11 or not cpf.isdigit() or
                        mes > 12 or mes < 1 or hora > 24 or hora < 0):
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
                if ((identificador <= 0) or not (0 >= dia > 31)
                        or not (0 >= mes > 12) or not (0 > hora > 24)):
                    raise ValueError
                return identificador, dia, mes, hora
            except ValueError:
                print("Informacoes invalidas. preencha novamente, por favor.")

    @staticmethod
    def tela_lista_aluguel_mes():
        print("Você escolheu visualizar os alugueis "
              "de um determinado mês.")
        while True:
            try:
                mes = int(input("Informe o dia, por favor: "))
                if mes < 1 or mes > 12:
                    raise ValueError
                return mes
            except ValueError:
                print("Dados oferecidos inválidos. "
                      "Preencha novamente, por favor.")

    @staticmethod
    def tela_recibo(nome: str, cpf: str, esporte: str,
                    dia: int, mes: int, horario: int):
        print('-'*35)
        print("Quadra de {}".format(esporte))
        print("alugada por {} inscrita no CPF {}".format(nome, cpf))
        print("para o dia {}/{} às {} horas.".format(dia, mes, horario))

    @staticmethod
    def tela_lista_aluguel_dia():
        print("Você escolheu visualizar os alugueis "
              "de um determinado dia.")
        while True:
            try:
                dia = int(input("Informe o dia, por favor: "))
                if dia < 1 or dia > 31:
                    raise ValueError
                return dia
            except ValueError:
                print("Dados oferecidos inválidos. "
                      "Preencha novamente, por favor.")
