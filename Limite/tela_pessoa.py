from Controle.controlador_pessoa import ControladorPessoa


class TelaPessoa:
    def __init__(self, controlador: ControladorPessoa):
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
        self.pede_dados(escolha)

    @staticmethod
    def le_num_inteiro(mensagem: str = "",
                       inteiros_validos: list = None):
        while True:
            try:
                inteiro = int(input(mensagem))
                if inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto. "
                      "Digite um valor válido, por favor.")
                print("Valores válidos:", inteiros_validos)

    def pede_dados(self, escolha):
        if escolha == 1:
            print("Você escolheu cadastrar um novo usuário."
                  "Informe os dados do usuário, por favor.")
            while True:
                try:
                    nome = str(input("Nome: "))
                    cpf = int(input("CPF: "))
                    telefone = int(input("Telefone: "))
                    email = str(input("E-mail: "))
                    if nome == "" or email == "":
                        raise ValueError
                    print(self.__controlador.add_pessoa(nome, cpf, telefone, email))
                    self.mostra_opcoes()
                except ValueError:
                    print("Dados oferecidos inválidos. "
                          "Preencha novamente, por favor.")
        elif escolha == 2:
            print("Você escolheu excluir um usuário. "
                  "Informe o CPF do usuário, por favor (Exemplo: 00000000800).")
            while True:
                try:
                    cpf = int(input("CPF: "))
                    if len(str(cpf)) != 11:
                        raise ValueError
                    print(self.__controlador.remove_pessoa(cpf))
                    self.mostra_opcoes()
                except ValueError:
                    print("CPF inválido. preencha novamente, por favor.")
        elif escolha == 3:
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
                    print(self.__controlador.edit_pessoa(cpf, nome, telefone, email))
                    self.mostra_opcoes()
                except ValueError:
                    print("CPF inválido. preencha novamente, por favor.")
        elif escolha == 4:
            print("Você escolheu visualizar todos os usuários cadastrados.")
            for pessoa in self.__controlador.lista_pessoas:
                print(pessoa)
            self.mostra_opcoes()
        elif escolha == 5:
            print("Você escolheu encontrar um usuário cadastrado.")
            try:
                cpf = int(input("Por favor, informe o CPF do usuário desejado."))
                if len(str(cpf)) != 11:
                    raise ValueError
                print(self.__controlador.encontrar_pessoa(cpf))
                self.mostra_opcoes()
            except ValueError:
                print("CPF inválido. preencha novamente, por favor.")
        # else:
            # Código para voltar pro menu inicial.









