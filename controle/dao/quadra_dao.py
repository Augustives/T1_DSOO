
from controle.dao.abc_dao import DAO

class QuadraDAO(DAO):
    def __init__(self):
        super().__init__("quadra.pkl")

    def add_quadra(self, quadra : Quadra):
        if isinstance(quadra.identificador, int) and (quadra is not None) and isinstance(quadra, Quadra):
            super().add(quadra.identificador, quadra)

    def get(self, identificador):
        if isinstance(identificador, int):
            return super().get(identificador)

    def remove(self, identificador):
        if isinstance(identificador, int):
            super().remove(identificador)