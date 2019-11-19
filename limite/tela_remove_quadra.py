from limite.abstract_remove_quadra import AbstractRemoveQuadra


class TelaRemoveQuadra(AbstractRemoveQuadra):
    def __init__(self, nome_tela: str, texto_entradas: list, texto_botao: str):
        super().__init__(nome_tela, texto_entradas, texto_botao)
