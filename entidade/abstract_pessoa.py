from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    @abstractmethod
    def cpf(self):
        pass

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf):
        pass

    @property
    @abstractmethod
    def telefone(self):
        pass

    @telefone.setter
    @abstractmethod
    def telefone(self, telefone):
        pass

    @property
    @abstractmethod
    def email(self):
        pass

    @email.setter
    @abstractmethod
    def email(self, email):
        pass
