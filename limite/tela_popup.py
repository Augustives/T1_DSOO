import PySimpleGUI as sg

class Popup():
    def __init__(self, texto: str):
        sg.Popup('Aviso !', texto)