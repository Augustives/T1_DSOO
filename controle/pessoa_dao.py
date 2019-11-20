from controle.abc_dao import DAO


class PessoaDAO(DAO):
    from entidade.pessoa import Pessoa
    def __init__(self):
        super().__init__("pessoa.pkl")

    def add(self, pessoa : Pessoa):
        if isinstance(pessoa.cpf, int) and (pessoa is not None) and isinstance(pessoa, Pessoa):
            super().add(pessoa.cpf, pessoa)

    def get(self, key):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)

