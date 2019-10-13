from Entidade.pessoa import Pessoa
from Entidade.pessoa_duplicada_exception import PessoaDuplicadaException
from pessoa_nao_cadastrada_exception import PessoaNaoCadastradaException
from Limite.tela_pessoa import TelaPessoa


class ControladorPessoa:
    def __init__(self):
        self.__tela_pessoa = TelaPessoa(self)
        self.__lista_pessoas = list()

    def add_pessoa(self, nome: str, cpf: int, telefone: int, email: str):
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                raise PessoaDuplicadaException

        pessoa_incluida = Pessoa(nome, cpf, telefone, email)
        self.__lista_pessoas.append(pessoa_incluida)
        return "Usuário cadastrado com sucesso."

    def remove_pessoa(self, cpf: int):
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                self.__lista_pessoas.remove(pessoa)
                return "Usuário removido com sucesso."

        raise PessoaNaoCadastradaException

    def edit_pessoa(self, cpf: int, nome, telefone, email):
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                if nome != "":
                    pessoa.nome = nome
                if telefone != "":
                    try:
                        telefone = int(telefone)
                        pessoa.telefone = telefone
                    except ValueError:
                        return "Telefone inválido."
                if email != "":
                    pessoa.email = email
                return "INFORMAÇÕES ATUALIZADAS:\n " \
                       "CPF: {}\n " \
                       "Nome: {}\n " \
                       "Telefone: {}\n " \
                       "Email: {}".format(pessoa.cpf, pessoa.nome, pessoa.telefone, pessoa.email)

    def encontrar_pessoa(self, cpf: int):
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                return "DADOS DO USUÁRIO:\n " \
                       "CPF: {}\n " \
                       "Nome: {}\n " \
                       "Telefone: {}\n " \
                       "Email: {}".format(pessoa.cpf, pessoa.nome, pessoa.telefone, pessoa.email)

    @property
    def lista_pessoas(self):
        return self.__lista_pessoas

    def abre_tela_pessoa(self):
        self.__tela_pessoa.mostra_opcoes()
