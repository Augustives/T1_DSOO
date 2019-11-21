from entidade.pessoa import Pessoa
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException
from controle.abstract_controlador_pessoa import AbstractControladorPessoa
from controle.pessoa_dao import PessoaDAO


class ControladorPessoa(AbstractControladorPessoa):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_pessoa import TelaPessoa
        super().__init__()
        self.__pessoas_DAO = PessoaDAO()
        self.__lista_nomes = list()
        for pessoa in self.__pessoas_DAO.get_all():
            lista = []
            lista.append(pessoa.nome)
            self.__lista_nomes.append(lista)
        self.__tela_pessoa = TelaPessoa(self, 'Tela Pessoa',
                                        ['Cadastrar Usuário', 'Remover Usuário',
                                         'Editar Usuário',
                                         'Dados Pessoa', 'Voltar'],
                                        self.__lista_nomes)
        self.__controlador_principal = controlador_principal

    def inicia(self):
        self.abre_tela_pessoa()

    def add_pessoa(self):
        from limite.tela_add_edit_pessoa import TelaAddEditPessoa
        tela_add_pessoa = TelaAddEditPessoa('Cadastrar Usuário',
                                            ['Nome', 'CPF', 'Telefone', 'E-mail'],
                                            'Cadastrar')
        nome, cpf, telefone, email = tela_add_pessoa.mostra_opcoes()
        try:
            if (nome == "" or email == "" or
                    len(cpf) != 11 or not cpf.isdigit()):
                raise ValueError
        except ValueError:
            self.abre_tela_pessoa()
        try:
            for pessoa in self.__pessoas_DAO.get_all():
                if pessoa.nome == nome:
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Pessoa já cadastrada.")
            self.abre_tela_pessoa()

        pessoa_incluida = Pessoa(nome, cpf, telefone, email)
        self.__pessoas_DAO.add(pessoa_incluida)
        self.__lista_nomes.append(pessoa_incluida.nome)
        print(self.__pessoas_DAO.get_all(), self.__lista_nomes)
        print("Usuário cadastrado com sucesso.")
        print(self.__lista_pessoas)
        print(self.__lista_nomes)
        self.abre_tela_pessoa()

    def remove_pessoa(self, nome: str):
        from limite.tela_remove_pessoa import TelaRemovePessoa
        tela_confirmacao = TelaRemovePessoa('Remover Usuário',
                                            'Você tem certeza que deseja \n '
                                            'excluir esse cadastro?')
        confirmacao = tela_confirmacao.mostra_opcoes()
        if confirmacao == 1:
            for pessoa in self.__pessoas_DAO.get_all():
                if pessoa.nome == nome:
                    self.__pessoas_DAO.remove(pessoa)
                    for i in range(len(self.__lista_nomes)):
                        if self.__lista_nomes[i][0] == nome:
                            self.__lista_nomes.pop(i)

                    print("Usuário removido com sucesso.")
                    self.abre_tela_pessoa()
            print("Usuário inexistente.")
            self.abre_tela_pessoa()
        else:
            self.abre_tela_pessoa()

    def edit_pessoa(self, nome_escolhido: str):
        from limite.tela_add_edit_pessoa import TelaAddEditPessoa
        tela_edit_pessoa = TelaAddEditPessoa('Editar Usuário',
                                             ['Nome', 'CPF', 'Telefone', 'E-mail'],
                                             'Alterar Informações')
        novo_nome, cpf, telefone, email = tela_edit_pessoa.mostra_opcoes()
        for pessoa in self.__lista_pessoas:
            if pessoa.nome == nome_escolhido:
                if novo_nome != "":
                    pessoa.nome = novo_nome
                    self.__lista_nomes[self.__lista_nomes.index(nome_escolhido)] \
                        = novo_nome
                if telefone != "":
                    try:
                        telefone = int(telefone)
                        pessoa.telefone = telefone
                    except ValueError:
                        print("Telefone inválido.")
                if email != "":
                    pessoa.email = email
                self.abre_tela_pessoa()
        print("Usuário inexistente.")
        self.abre_tela_pessoa()

    def dados_pessoa(self, nome: str):
        from limite.tela_dados_pessoa import TelaDadosPessoa
        for pessoa in self.__lista_pessoas:
            if pessoa.nome == nome:
                tela_dados_pessoa = TelaDadosPessoa('Dados do Usuário',
                                                    [pessoa.nome, pessoa.cpf,
                                                     pessoa.telefone, pessoa.email])
                voltar = tela_dados_pessoa.mostra_opcoes()
                if voltar == 1:
                    self.abre_tela_pessoa()
        print("Usuário inexistente.")
        self.abre_tela_pessoa()

    @property
    def lista_pessoas(self):
        return self.__lista_pessoas

    @property
    def lista_nomes(self):
        return self.__lista_nomes

    def voltar(self):
        self.__controlador_principal.inicia()

    def abre_tela_pessoa(self):
        escolhas = {1: self.add_pessoa, 2: self.remove_pessoa,
                    3: self.edit_pessoa,
                    4: self.dados_pessoa, 5: self.voltar}
        escolha, nome = self.__tela_pessoa.mostra_opcoes()
        if escolha is None:
            escolha = 6
        funcao_escolhida = escolhas[escolha]
        if escolha in [1, 5]:
            funcao_escolhida()
        else:
            try:
                funcao_escolhida(nome[0][0])
            except IndexError:
                self.abre_tela_pessoa()

    def encontra_pessoa(self, nome):
        for pessoa in self.__lista_pessoas:
            if pessoa.nome == nome:
                return pessoa
