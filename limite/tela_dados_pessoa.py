from limite.abstract_dados import AbstractDados


class TelaDadosPessoa(AbstractDados):
    def __init__(self, nome_tela: str, lista_dados: list):
        super().__init__(nome_tela, lista_dados)
