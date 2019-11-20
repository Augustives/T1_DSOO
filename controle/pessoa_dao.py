from controle.abc_dao import DAO

class PessoaDAO(DAO):
    from entidade.pessoa import Pessoa
    def __init__(self):
        super().__init__("pessoa.pkl")

    def add_pessoa(self, pessoa : Pessoa):
        if isinstance(pessoa.cpf, int) and (pessoa is not None) and isinstance(pessoa, Pessoa):
            super().add(pessoa.cpf, pessoa)

    def get(self, cpf):
        if isinstance(cpf, int):
            return super().get(cpf)

    def remove(self, cpf):
        if isinstance(cpf, int):
            super().remove(cpf)

    def lista(self):
        return super().get_all()