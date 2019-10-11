from Controle.abstract_controlador_aluguel import AbstractControladorAluguel
from Entidade.quadra import Quadra
from Entidade.pessoa import Pessoa

class ControladorAluguel(AbstractControladorAluguel):
    def __init__(self):
        super().__init__()
        self.__lista_ano1 = [[],[],[],[],[],[],[],[],[],[],[],[]]

