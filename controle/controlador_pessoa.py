from entidade.pessoa import Pessoa
from entidade.pessoa_duplicada_exception import PessoaDuplicadaException
from limite.tela_pessoa import TelaPessoa
from controle.controlador_principal import ControladorPrincipal
from controle.abstract_controlador_pessoa import AbstractControladorPessoa


class ControladorPessoa(AbstractControladorPessoa):
    def __init__(self):
        super().__init__()
        self.__tela_pessoa = TelaPessoa(self)
        self.__lista_pessoas = list()

    def inicia(self):
        self.abre_tela_pessoa()

    def add_pessoa(self):
        nome, cpf, telefone, email = self.__tela_pessoa.tela_add_pessoa()
        try:
            for pessoa in self.__lista_pessoas:
                if pessoa.cpf == cpf:
                    raise PessoaDuplicadaException
        except PessoaDuplicadaException:
            print("Pessoa já cadastrada.")
            self.abre_tela_pessoa()

        pessoa_incluida = Pessoa(nome, cpf, telefone, email)
        self.__lista_pessoas.append(pessoa_incluida)
        print("Usuário cadastrado com sucesso.")
        self.abre_tela_pessoa()

    def remove_pessoa(self):
        cpf = self.__tela_pessoa.tela_remove_pessoa()
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                self.__lista_pessoas.remove(pessoa)
                print("Usuário removido com sucesso.")
                self.abre_tela_pessoa()
        print("Usuário inexistente.")
        self.abre_tela_pessoa()

    def edit_pessoa(self):
        cpf, nome, telefone, email = self.__tela_pessoa.tela_edit_pessoa()
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                if nome != "":
                    pessoa.nome = nome
                if telefone != "":
                    try:
                        telefone = int(telefone)
                        pessoa.telefone = telefone
                    except ValueError:
                        print("Telefone inválido.")
                if email != "":
                    pessoa.email = email
                print("INFORMAÇÕES ATUALIZADAS:\n "
                      "CPF: {}\n "
                      "Nome: {}\n "
                      "Telefone: {}\n "
                      "Email: {}".format(pessoa.cpf, pessoa.nome,
                                         pessoa.telefone, pessoa.email))
                self.abre_tela_pessoa()
        print("Usuário inexistente.")
        self.abre_tela_pessoa()

    def encontrar_pessoa(self):
        cpf = self.__tela_pessoa.tela_encontrar_pessoa()
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                print("DADOS DO USUÁRIO:\n "
                      "CPF: {}\n "
                      "Nome: {}\n "
                      "Telefone: {}\n "
                      "Email: {}".format(pessoa.cpf, pessoa.nome, pessoa.telefone, pessoa.email))
                self.abre_tela_pessoa()
        print("Usuário inexistente.")
        self.abre_tela_pessoa()

    @property
    def lista_pessoas(self):
        return self.__lista_pessoas

    def listar_pessoas(self):
        self.__tela_pessoa.tela_listar_pessoas()
        self.abre_tela_pessoa()

    @staticmethod
    def voltar():
        ControladorPrincipal.inicia()

    def abre_tela_pessoa(self):
        escolhas = {1: self.add_pessoa, 2: self.remove_pessoa,
                    3: self.edit_pessoa, 4: self.listar_pessoas,
                    5: self.encontrar_pessoa, 0: self.voltar}
        escolha = self.__tela_pessoa.mostra_opcoes()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()
