from limite.abstract_sim_nao import AbstractSimNao


class TelaRemoveAluguel(AbstractSimNao):
    def __init__(self, nome_tela: str, texto_confirmacao: str):
        super().__init__(nome_tela, texto_confirmacao)
