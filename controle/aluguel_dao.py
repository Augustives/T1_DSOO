from controle.abc_dao import DAO
from entidade.aluguel import Aluguel


class AlugelDAO(DAO):
    def __init__(self):
        super().__init__("aluguel.pkl")

    def add(self, aluguel: Aluguel):
        if isinstance(aluguel, Aluguel):
            super().add("{} {} {} --> {} / {} - {}".format(aluguel.quadra.esporte,
                                                           aluguel.quadra.tipo,
                                                           aluguel.quadra.identificador,
                                                           aluguel.dia,
                                                           aluguel.mes,
                                                           aluguel.hora),
                        aluguel)

    def get(self, key: int):
        return super().get(key)

    def remove(self, aluguel: Aluguel):
        super().remove("{} {} {} --> {} / {} - {}".format(aluguel.quadra.esporte,
                                                          aluguel.quadra.tipo,
                                                          aluguel.quadra.identificador,
                                                          aluguel.dia,
                                                          aluguel.mes,
                                                          aluguel.hora))



#Vamo precisar de uma key pros alugueis, ai tem q ver se numeramos eles, ou fazemos a key com oq