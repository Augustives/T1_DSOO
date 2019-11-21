import PySimpleGUI as sg


class AbstractOpcoes:
    def __init__(self, nome_tela: str, texto_botoes: list):
        self.__janela = None
        self.__nome_tela = nome_tela
        self.__texto_botoes = texto_botoes

    def configura(self, nome_tela: str, texto_botoes: list):
        sg.ChangeLookAndFeel("Reddit")

        layout = []
        for i in range(len(texto_botoes)):
            layout.append([sg.Button(texto_botoes[i], size=(200, 4),
                           button_color=('#000', '#5CBEFF'),
                           font=('Helvetica', 14), key=i+1)])

        self.__janela = sg.Window(nome_tela, layout, size=(500, 130*len(texto_botoes)),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__nome_tela, self.__texto_botoes)
        button, values = self.__janela.Read()
        self.__janela.Close()
        return button

    def fechar(self):
        self.__janela.Close()




