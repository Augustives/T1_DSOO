from Limite.abstract_tela import AbstractTela


class TelaInicial(AbstractTela):
    from Controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador: ControladorPrincipal):
        super().__init__()
        self.__controlador = controlador

    def mostra_opcoes(self):
        print("---------- MENU INICIAL ----------")
        print("1 - Informações sobre usuários")
        print("2 - Informações sobre quadras")
        print("3 - Informações sobre aluguéis")
        print("----------------------------------")

        escolha = self.le_num_inteiro("Escolha uma das opções:",
                                      [1, 2, 3])
        return escolha
