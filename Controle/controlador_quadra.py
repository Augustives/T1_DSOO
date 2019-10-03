from Controle.abstract_controlador_quadra import AbstractControladorQuadra

class ControladorQuadra(AbstractControladorQuadra):
    def __init__(self):
        super().__init__()
        self.__lista_quadras = []

    