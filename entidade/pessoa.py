from entidade.abstract_pessoa import AbstractPessoa


class Pessoa(AbstractPessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        super().__init__()
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
