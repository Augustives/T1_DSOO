import PySimpleGUI as sg


class TelaAddAluguel:
    def __init__(self, nome_tela: str, lista_pessoas: list,
                 lista_quadras: list):
        self.__nome_tela = nome_tela
        self.__lista_pessoas = lista_pessoas
        self.__lista_quadras = lista_quadras
        self.__janela = None

    def configura(self, lista_pessoas, lista_quadras):
        sg.ChangeLookAndFeel("Reddit")

        horarios = ['00:00', '00:30', '01:00', '01:30', '02:30', '03:00', '03:30',
                    '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00',
                    '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00',
                    '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30',
                    '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00',
                    '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30',
                    '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']
        layout = [
                    [sg.Text('Usuário', size=(15, 1)), sg.Listbox(values=lista_pessoas,
                                                                  size=(200, 4), font=('Helvetica', 14))],
                    [sg.Text('Quadra', size=(15, 1)), sg.Listbox(values=lista_quadras,
                                                                 size=(200, 4), font=('Helvetica', 14))],
                    [sg.Text('Mês', size=(15, 1)), sg.Listbox(values=range(1, 13),
                                                              size=(200, 4), font=('Helvetica', 14))],
                    [sg.Text('Dia', size=(15, 1)), sg.Listbox(values=range(1, 32),
                                                              size=(200, 4), font=('Helvetica', 14))],
                    [sg.Text('Horário', size=(15, 1)), sg.Listbox(values=horarios,
                                                                  size=(200, 4), font=('Helvetica', 14))],
                    [sg.Button('Realizar Aluguel', size=(200, 4),
                               button_color=('#000', '#7D7D7D'),
                               font=('Helvetica', 14))]
                 ]

        self.__janela = sg.Window(self.__nome_tela, layout, size=(500, 900),
                                  element_justification="center")

    def mostra_opcoes(self):
        self.configura(self.__lista_pessoas, self.__lista_quadras)
        button, dict_valores = self.__janela.Read()
        self.__janela.Close()
        usuario, quadra, mes, dia, horario = dict_valores.values()
        if (usuario is None and quadra is None
                and mes is None and dia is None and horario is None):
            return None, None, None, None, None
        return usuario[0], quadra[0], mes[0], dia[0], horario[0]
