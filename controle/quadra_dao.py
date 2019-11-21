from controle.abc_dao import DAO


class QuadraDAO(DAO):
    from entidade.quadra import Quadra

    def __init__(self):
        super().__init__("quadra.pkl")

    def add(self, quadra : Quadra):
        if isinstance(quadra.identificador, int) and (quadra is not None) and isinstance(quadra, Quadra):
            super().add(quadra.identificador, quadra)

    def get(self, key):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)

