import PySimpleGUI as sg


class TelaDadosListagem:
    def __init__(self, nome_tela: str, lista_dados: list):
        self.__nome_tela = nome_tela
        self.__lista_dados = lista_dados
        self.__janela = None

    def configura(self, lista_dados):
        sg.ChangeLookAndFeel("Reddit")

        layout = [
                    [sg.Listbox(values=lista_dados,
                                size=(200, 4), font=('Helvetica', 14))],

                    [sg.Button('Voltar', size=(200, 4),
                               button_color=('#000', '#7D7D7D'),
                               font=('Helvetica', 14), key=1)]
        ]

        self.__janela = sg.Window(self.__nome_tela, layout, size=(500, 500),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__lista_dados)
        button, values = self.__janela.Read()
        self.__janela.Close()
        return button
