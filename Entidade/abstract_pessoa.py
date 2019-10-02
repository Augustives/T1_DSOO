from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, telefone: int, email: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        pass

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        self.__nome = nome

    @property
    @abstractmethod
    def cpf(self)
        return self.__cpf

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    @abstractmethod
    def telefone(self):
        return self.__telefone

    @telefone.setter
    @abstractmethod
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    @abstractmethod
    def email(self):
        return self.__email

    @email.setter
    @abstractmethod
    def email(self, email):
        self.__email = email