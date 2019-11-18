import PySimpleGUI as sg


class AbstractOpcoes:
    def __init__(self, nome_tela: str, texto_botoes: list):
        self.__janela = None
        self.configura(nome_tela, texto_botoes)

    def configura(self, nome_tela: str, texto_botoes: list):
        sg.ChangeLookAndFeel("Reddit")

        layout = []
        for i in range(len(texto_botoes)):
            layout.append([sg.Button(texto_botoes[i], size=(200, 4),
                           button_color=('#000', '#7D7D7D'),
                           font=('Helvetica', 14), key=i+1)])

        self.__janela = sg.Window(nome_tela, layout, size=(500, 80*len(texto_botoes)),
                                  element_justification="center")

    def mostra_opcoes(self):
        while True:
            button, values = self.__janela.Read()
            if button is None or button == 6:
                self.__janela.close()
                return 6

            return button




