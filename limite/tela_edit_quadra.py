from limite.abstract_add_edit_quadra import AbstractAddEditQuadra


class TelaEditQuadra(AbstractAddEditQuadra):
    def __init__(self, nome_tela: str, texto_entradas: list, texto_botao: str):
        super().__init__(nome_tela, texto_entradas, texto_botao)
