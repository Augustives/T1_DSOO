from limite.abstract_listagem import AbstractListagem


class TelaPessoa(AbstractListagem):
    from controle.controlador_pessoa import ControladorPessoa

    def __init__(self, controlador: ControladorPessoa,
                 nome_tela: str, texto_botoes: list,
                 lista_pessoas: list):
        super().__init__(nome_tela, texto_botoes, lista_pessoas)
        self.__controlador = controlador
