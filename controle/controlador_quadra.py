from controle.abstract_controlador_quadra import AbstractControladorQuadra
from entidade.quadra import Quadra


class ControladorQuadra(AbstractControladorQuadra):
    def __init__(self):
        super().__init__()
        self.__lista_quadras = []

    def add_quadra(self,  esporte: str, tipo: str, identificador: int):
        identificador = Quadra(esporte, tipo, identificador)
        self.__lista_quadras.append(identificador)

    def remove_quadra(self, identificador):
        if identificador in self.__lista_quadras:
            self.lista_quadras().remove(identificador)

    def edit_quadra(self):
        pass

    def lista_quadras(self):
        return self.__lista_quadras

    def lista_quadras_esporte(self, esporte):
        self.__lista_esporte = []
        for quadra in self.__lista_quadras:
            if quadra.esporte == esporte:
                self.__lista_esporte.append(quadra)
        return self.__lista_esporte

    def lista_quadras_tipo(self, tipo):
        self.__lista_tipo = []
        for quadra in self.__lista_quadras:
            if quadra.tipo == tipo:
                self.__lista_tipo.append(quadra)
        return self.__lista_tipo

    def abre_tela_quadras(self):
        pass

    