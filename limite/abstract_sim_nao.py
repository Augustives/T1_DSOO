import PySimpleGUI as sg


class AbstractSimNao:
    def __init__(self, nome_tela: str, texto_confirmacao: str):
        self.__nome_tela = nome_tela
        self.__texto_confirmacao = texto_confirmacao
        self.__janela = None

    def configura(self, texto_confirmacao):
        sg.ChangeLookAndFeel("Reddit")

        layout = [[sg.Txt(texto_confirmacao, font=('Helvetica', 14), size=(200, 3),
                          justification="center")],
                  [sg.Button('Sim', size=(200, 4),
                             button_color=('#000', '#7D7D7D'),
                             font=('Helvetica', 14), key=1)],
                  [sg.Button('Não', size=(200, 4),
                             button_color=('#000', '#7D7D7D'),
                             font=('Helvetica', 14), key=2)]
                  ]

        self.__janela = sg.Window(self.__nome_tela, layout, size=(500, 300),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__texto_confirmacao)
        button, values = self.__janela.Read()
        self.__janela.Close()
        return button


