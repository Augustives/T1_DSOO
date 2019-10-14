from Controle.controlador_quadra import ControladorQuadra
from Limite.abstract_tela import AbstractTela

class TelaQuadra(AbstractTela):
    def __init__(self, controlador: ControladorQuadra):
        super().__init__()
        self.__controlador = controlador

    def mostra_opcoes(self):
        print("---------- CADASTRO DE QUADRAS ----------")
        print("1 - Cadastrar quadra")
        print("2 - Excluir quadra")
        print("3 - Alterar informações da quadra")
        print("4 - Listar todas as quadras")
        print("5 - Listar quadras por esporte")
        print("0 - Voltar")
        print("-----------------------------------------")

        escolha = self.le_num_inteiro("Escolha uma das opções:",
                                      [1, 2, 3, 4, 5, 0])
        return escolha

    @staticmethod
    def tela_add_quadra():
        print("Você escolheu cadastrar uma nova quadra."
              "Informe os dados da quadra, por favor.")
        while True:
            try:
                esporte = str(input("Esporte: "))
                tipo = str(input("Tipo: "))
                if esporte == "" or tipo == "":
                    raise ValueError
                return esporte, tipo
            except ValueError:
                print("Dados oferecidos inválidos. "
                      "Preencha novamente, por favor.")

    @staticmethod
    def tela_remove_quadra():
        print("Você escolheu excluir uma quadra. "
              "Informe o Identificador da quadra, por favor (Exemplo: 1).")
        while True:
            try:
                identificador = int(input("Identificador: "))
                if identificador not in self.__controlador.lista_identificador:
                    raise ValueError
                return identificador
            except ValueError:
                print("Identificador inválido. preencha novamente, por favor.")

    @staticmethod
    def tela_edit_quadra():
        print("Você escolheu alterar as informações de uma quadra existente.")
        while True:
            try:
                identificador = int(input("Por favor, informe o Identificador da quadra desejada."))
                if identificador not in self.__controlador.lista_identificador:
                    raise ValueError
                print("Por favor, forneça os dados atualizados da quadra.\n"
                      "Caso queira manter os dados atuais, "
                      "apenas deixe o campo a ser preenchido em branco.")
                esporte = str(input("Esporte: "))
                tipo = str(input("Tipo: "))
                identificador = int(input("Identificador: "))
                return esporte, tipo, identificador
            except ValueError:
                print("Identificador inválido. preencha novamente, por favor.")

    def tela_listar_quadras(self):
        print("Você escolheu visualizar todas as quadras cadastradas.")
        for quadra in self.__controlador.lista_quadras:
            print("-"*30)
            print(quadra.esporte)
            print(quadra.tipo)
            print(quadra.identificador)

    def tela_listar_quadras_esporte(self, esporte):
        print("Você escolheu visualizar todas as quadras casdastrada com esse esporte.")
        for quadra in self.__controlador.lista_quadras:
            if quadra.esporte == esporte:
                print("-" * 30)
                print(quadra.esporte)
                print(quadra.tipo)
                print(quadra.identificador)
