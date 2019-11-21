from controle.abc_dao import DAO
from entidade.aluguel import Aluguel

class AlugelDAO(DAO):
    def __init__(self):
        super().__init__("aluguel.pkl")

    def add(self, aluguel: Aluguel):
        if isinstance(aluguel, Aluguel):
            super().add()

    def get(self, key: int):
            return super().get(key)

    def remove(self, key):
            super().remove(key)



#Vamo precisar de uma key pros alugueis, ai tem q ver se numeramos eles, ou fazemos a key com oq