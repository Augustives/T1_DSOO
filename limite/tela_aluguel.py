from limite.abstract_listagem import AbstractListagem


class TelaAluguel(AbstractListagem):
    from controle.controlador_aluguel import ControladorAluguel

    def __init__(self, controlador: ControladorAluguel,
                 nome_tela: str, texto_botoes: list, lista_alugueis: list):
        super().__init__(nome_tela, texto_botoes, lista_alugueis)
        self.__controlador = controlador
