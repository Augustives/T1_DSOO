from controle.abc_dao import DAO
from entidade.quadra import Quadra


class QuadraDAO(DAO):
    def __init__(self):
        super().__init__('quadras.pkl')

    def add(self, quadra: Quadra):
        if isinstance(quadra, Quadra):
            super().add(quadra.identificador, quadra)

    def get(self, key: int):
            return super().get(key)

    def remove(self, key):
            super().remove(key)

