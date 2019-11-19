from controle.controlador_quadra import ControladorQuadra
from limite.abstract_listagem import AbstractListagem


class TelaQuadra(AbstractListagem):
    def __init__(self, controlador: ControladorQuadra,
                 nome_tela: str, texto_botoes: list, lista_quadras: list):
        super().__init__(nome_tela, texto_botoes, lista_quadras)
        self.__controlador = controlador

    @staticmethod
    def tela_add_quadra():
        print("Você escolheu cadastrar uma nova quadra."
              "Informe os dados da quadra, por favor.")
        while True:
            try:
                esporte = str(input("Esporte: "))
                tipo = str(input("Tipo: "))
                identificador = int(input("Identificador: "))
                if esporte == "" or tipo == "" or identificador <= 0:
                    raise ValueError
                return esporte, tipo, identificador
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
                if identificador <= 0:
                    raise ValueError
                return identificador
            except ValueError:
                print("Identificador inválido. preencha novamente, por favor.")

    @staticmethod
    def tela_edit_quadra():
        print("Você escolheu alterar as informações de uma quadra existente.")
        while True:
            try:
                identificador = int(input("Por favor, informe o Identificador da quadra desejada: "))
                if identificador <= 0:
                    raise ValueError
                print("Por favor, forneça os dados atualizados da quadra.\n"
                      "Caso queira manter os dados atuais, "
                      "apenas deixe o campo a ser preenchido em branco.")
                esporte = str(input("Esporte: "))
                tipo = str(input("Tipo: "))
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

    def tela_listar_quadras_esporte(self):
        esporte = str(input("Por favor, informe o esporte desejado: "))
        print("Você escolheu visualizar todas as quadras cadastrada com esse esporte.")
        for quadra in self.__controlador.lista_quadras:
            if quadra.esporte == esporte:
                print("-" * 30)
                print(quadra.esporte)
                print(quadra.tipo)
                print(quadra.identificador)
