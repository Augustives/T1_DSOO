from entidade.abc_dao import DAO
from entidade.pessoa import Pessoa


class PessoaDAO(DAO):
    def __init__(self):
        super().__init__("pessoa.pkl")

    def add(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            super().add(pessoa.cpf, pessoa)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        super().remove(key)

    def edit(self, pessoa_antiga: Pessoa, pessoa_nova: Pessoa):
        super().remove(pessoa_antiga.cpf)
        super().add(pessoa_nova.cpf, pessoa_nova)
