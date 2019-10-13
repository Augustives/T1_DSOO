from controle.controlador_pessoa import ControladorPessoa
from limite.abstract_tela import AbstractTela


class TelaPessoa(AbstractTela):
    def __init__(self, controlador: ControladorPessoa):
        super().__init__()
        self.__controlador = controlador

    def mostra_opcoes(self):
        print("---------- CADASTRO DE USUÁRIO ----------")
        print("1 - Cadastrar usuário")
        print("2 - Excluir usuário")
        print("3 - Alterar informações do usuário")
        print("4 - Listar todos os usuários")
        print("5 - Encontrar usuário cadastrado.")
        print("0 - Voltar")
        print("-----------------------------------------")

        escolha = self.le_num_inteiro("Escolha uma das opções:",
                                      [1, 2, 3, 4, 5, 0])
        return escolha

    @staticmethod
    def tela_add_pessoa():
        print("Você escolheu cadastrar um novo usuário."
              "Informe os dados do usuário, por favor.")
        while True:
            try:
                nome = str(input("Nome: "))
                cpf = int(input("CPF: "))
                telefone = int(input("Telefone: "))
                email = str(input("E-mail: "))
                if nome == "" or email == "" or len(str(cpf)) != 11:
                    raise ValueError
                return nome, cpf, telefone, email
            except ValueError:
                print("Dados oferecidos inválidos. "
                      "Preencha novamente, por favor.")

    @staticmethod
    def tela_remove_pessoa():
        print("Você escolheu excluir um usuário. "
              "Informe o CPF do usuário, por favor (Exemplo: 00000000800).")
        while True:
            try:
                cpf = int(input("CPF: "))
                if len(str(cpf)) != 11:
                    raise ValueError
                return cpf
            except ValueError:
                print("CPF inválido. preencha novamente, por favor.")

    @staticmethod
    def tela_edit_pessoa():
        print("Você escolheu alterar as informações de um usuário existente.")
        while True:
            try:
                cpf = int(input("Por favor, informe o CPF do usuário desejado."))
                if len(str(cpf)) != 11:
                    raise ValueError
                print("Por favor, forneça os dados atualizados do usuário.\n"
                      "Caso queira manter os dados atuais, "
                      "apenas deixe o campo a ser preenchido em branco.")
                nome = str(input("Nome: "))
                telefone = str(input("Telefone: "))
                email = str(input("E-mail: "))
                return cpf, nome, telefone, email
            except ValueError:
                print("CPF inválido. preencha novamente, por favor.")

    def tela_listar_pessoas(self):
        print("Você escolheu visualizar todos os usuários cadastrados.")
        for pessoa in self.__controlador.lista_pessoas:
            print(pessoa)

    @staticmethod
    def tela_encontrar_pessoa():
        print("Você escolheu encontrar um usuário cadastrado.")
        try:
            cpf = int(input("Por favor, informe o CPF do usuário desejado."))
            if len(str(cpf)) != 11:
                raise ValueError
            return cpf
        except ValueError:
            print("CPF inválido. preencha novamente, por favor.")

