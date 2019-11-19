from entidade.pessoa import Pessoa
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException
from controle.abstract_controlador_pessoa import AbstractControladorPessoa


class ControladorPessoa(AbstractControladorPessoa):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_pessoa import TelaPessoa
        super().__init__()
        self.__lista_pessoas = list()
        self.__lista_nomes = list()
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
            for pessoa in self.__lista_pessoas:
                if pessoa.cpf == cpf:
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Pessoa já cadastrada.")
            self.abre_tela_pessoa()

        pessoa_incluida = Pessoa(nome, cpf, telefone, email)
        self.__lista_pessoas.append(pessoa_incluida)
        self.__lista_nomes.append(pessoa_incluida.nome)
        print("Usuário cadastrado com sucesso.")
        self.abre_tela_pessoa()

    def remove_pessoa(self, nome: str):
        from limite.tela_remove_pessoa import TelaRemovePessoa
        tela_confirmacao = TelaRemovePessoa('Tela Pessoa',
                                            'Você tem certeza que deseja \n '
                                            'excluir esse cadastro?')
        confirmacao = tela_confirmacao.mostra_opcoes()
        if confirmacao == 1:
            for pessoa in self.__lista_pessoas:
                if pessoa.nome == nome:
                    self.__lista_pessoas.remove(pessoa)
                    self.__lista_nomes.remove(pessoa.nome)
                    print("Usuário removido com sucesso.")
                    self.abre_tela_pessoa()
            print("Usuário inexistente.")
            self.abre_tela_pessoa()
        else:
            self.abre_tela_pessoa()

    def edit_pessoa(self, nome_escolhido: str):
        from limite.tela_add_edit_pessoa import TelaAddEditPessoa
        tela_add_pessoa = TelaAddEditPessoa('Editar Usuário',
                                            ['Nome', 'CPF', 'Telefone', 'E-mail'],
                                            'Cadastrar')
        novo_nome, cpf, telefone, email = tela_add_pessoa.mostra_opcoes()
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
                print("INFORMAÇÕES ATUALIZADAS:\n "
                      "CPF: {}\n "
                      "Nome: {}\n "
                      "Telefone: {}\n "
                      "Email: {}".format(pessoa.cpf, pessoa.nome,
                                         pessoa.telefone, pessoa.email))
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
            funcao_escolhida(nome[0][0])

    def encontra_pessoa(self, cpf):
        for pessoa in self.__lista_pessoas:
            if pessoa.cpf == cpf:
                return pessoa
