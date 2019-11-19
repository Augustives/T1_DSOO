import PySimpleGUI as sg


class AbstractRemoveQuadra:
    def __init__(self, nome_tela: str, texto_entradas: list, texto_botao: str):
        self.__nome_tela = nome_tela
        self.__texto_botao = texto_botao
        self.__texto_entradas = texto_entradas
        self.__janela = None

    def configura(self, texto_entradas, texto_botao):
        sg.ChangeLookAndFeel("Reddit")

        layout = [
                    [sg.Text('Por favor, informe o identificador.')],
                 ]
        for i in range(len(texto_entradas)):
            layout.append([sg.Text(texto_entradas[i], size=(15, 1)), sg.InputText()])

        layout.append([sg.Button(texto_botao, size=(200, 4),
                                 button_color=('#000', '#5CBEFF'),
                                 font=('Helvetica', 14))])

        self.__janela = sg.Window(self.__nome_tela, layout, size=(500, 300),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__texto_entradas, self.__texto_botao)
        botao, dict_valores = self.__janela.Read()
        self.__janela.Close()
        identificador = dict_valores.values()

        return identificador