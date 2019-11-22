from controle.controlador_quadra import ControladorQuadra
from limite.abstract_listagem import AbstractListagem


class TelaQuadra(AbstractListagem):
    def __init__(self, controlador: ControladorQuadra,
                 nome_tela: str, texto_botoes: list, lista_quadras: list):
        super().__init__(nome_tela, texto_botoes, lista_quadras)
        self.__controlador = controlador
