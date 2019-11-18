from limite.abstract_opcoes import AbstractOpcoes


class TelaInicial(AbstractOpcoes):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador: ControladorPrincipal,
                 nome_tela: str, texto_botoes: list):
        super().__init__(nome_tela, texto_botoes)
        self.__controlador = controlador

