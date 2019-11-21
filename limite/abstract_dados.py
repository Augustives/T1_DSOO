import PySimpleGUI as sg


class AbstractDados:
    def __init__(self, nome_tela: str, lista_dados: list):
        self.__nome_tela = nome_tela
        self.__lista_dados = lista_dados
        self.__janela = None

    def configura(self, lista_dados):
        sg.ChangeLookAndFeel("Reddit")

        layout = []
        for i in range(len(lista_dados)):
            layout.append([sg.Txt(lista_dados[i], font=('Helvetica', 14),
                                  size=(200, 3), justification="center")])

        layout.append([sg.Button('Voltar', size=(200, 4),
                                 button_color=('#000', '#5CBEFF'),
                                 font=('Helvetica', 14), key=1)])

        self.__janela = sg.Window(self.__nome_tela, layout, size=(500, 120*len(lista_dados)),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__lista_dados)
        button, values = self.__janela.Read()
        self.__janela.Close()
        return button
