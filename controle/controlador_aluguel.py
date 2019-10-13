from controle.abstract_controlador_aluguel import AbstractControladorAluguel
from entidade.quadra import Quadra
from entidade.pessoa import Pessoa

class ControladorAluguel(AbstractControladorAluguel):
    def __init__(self):
        super().__init__()
        self.__lista_ano1 = [[],[],[],[],[],[],[],[],[],[],[],[]]

