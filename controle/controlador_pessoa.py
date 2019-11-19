from entidade.pessoa import Pessoa
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException
from controle.abstract_controlador_pessoa import AbstractControladorPessoa


class ControladorPessoa(AbstractControladorPessoa):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_pessoa import TelaPessoa
        super().__init__()
        self.__lista_pessoas = list()
        self.__tela_pessoa = TelaPessoa(self, 'Tela Pessoa',
                                        ['Cadastrar Usuário', 'Remover Usuário',
                                         'Editar Usuário', 'Listar Pessoas',
                                         'Encontrar Pessoa', 'Voltar'],
                                        self.lista_pessoas)
        self.__controlador_principal = controlador_principal

    def inicia(self):
        self.abre_tela_pessoa()

    def add_pessoa(self):
        from limite.tela_add_pessoa import TelaAddPessoa
        tela_add_pessoa = TelaAddPessoa('Cadastrar Usuário',
                                        ['Nome', 'CPF', 'Telefone', 'E-mail'],
                                        'Cadastrar')
        nome, cpf, telefone, email = tela_add_pessoa.mostra_opcoes()
        try:
            for pessoa in self.__lista_pessoas:
                if pessoa.cpf == cpf:
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
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

    def dados_pessoa(self):
        cpf = self.__tela_pessoa.tela_dados_pessoa()
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                print("-" * 30)
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

    def voltar(self):
        self.__controlador_principal.inicia()

    def abre_tela_pessoa(self):
        escolhas = {1: self.add_pessoa, 2: self.remove_pessoa,
                    3: self.edit_pessoa, 4: self.listar_pessoas,
                    5: self.dados_pessoa, 6: self.voltar}
        escolha, nome = self.__tela_pessoa.mostra_opcoes()
        if escolha is None:
            escolha = 6
        funcao_escolhida = escolhas[escolha]
        if escolha in [1, 4, 6]:
            funcao_escolhida()
        else:
            print(nome)
            funcao_escolhida()

    def encontra_pessoa(self, cpf):
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                return pessoa
