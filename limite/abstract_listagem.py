import PySimpleGUI as sg


class AbstractListagem:
    def __init__(self, nome_tela: str,
                 texto_botoes: list, lista: list):
        self.__nome_tela = nome_tela
        self.__texto_botoes = texto_botoes
        self.__lista = lista
        self.__janela = None

    def configura(self, texto_botoes: list, lista: list):
        sg.ChangeLookAndFeel("Reddit")

        layout = [[sg.Listbox(values=lista,
                              size=(200, 4), font=('Helvetica', 14))]
                  ]
        for i in range(len(texto_botoes)):
            layout.append([sg.Button(texto_botoes[i], size=(200, 4),
                           button_color=('#000', '#7D7D7D'),
                           font=('Helvetica', 14), key=i+1)])

        self.__janela = sg.Window(self.__nome_tela, layout, size=(500, 700),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__texto_botoes, self.__lista)
        button, values = self.__janela.Read()
        self.__janela.Close()
        return button, values


