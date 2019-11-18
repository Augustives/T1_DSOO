from limite.abstract_opcoes import AbstractOpcoes


class TelaPessoa(AbstractOpcoes):
    from controle.controlador_pessoa import ControladorPessoa

    def __init__(self, controlador: ControladorPessoa,
                 nome_tela: str, texto_botoes: list):
        super().__init__(nome_tela, texto_botoes)
        self.__controlador = controlador

    @staticmethod
    def tela_add_pessoa():
        print("Você escolheu cadastrar um novo usuário. \n"
              "Informe os dados do usuário, por favor.")
        while True:
            try:
                nome = str(input("Nome: "))
                cpf = str(input("CPF: "))
                telefone = int(input("Telefone: "))
                email = str(input("E-mail: "))
                if (nome == "" or email == "" or
                        len(cpf) != 11 or not cpf.isdigit()):
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
                cpf = str(input("CPF: "))
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError
                return cpf
            except ValueError:
                print("CPF inválido. preencha novamente, por favor.")

    @staticmethod
    def tela_edit_pessoa():
        print("Você escolheu alterar as informações de um usuário existente.")
        while True:
            try:
                cpf = str(input("Por favor, informe o CPF do usuário desejado."))
                if len(cpf) != 11 or not cpf.isdigit():
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
            print("-"*30)
            print(pessoa.nome)
            print(pessoa.cpf)
            print(pessoa.telefone)
            print(pessoa.email)

    @staticmethod
    def tela_dados_pessoa():
        print("Você escolheu encontrar um usuário cadastrado.")
        try:
            cpf = str(input("Por favor, informe o CPF do usuário desejado."))
            if len(cpf) != 11 or not cpf.isdigit():
                raise ValueError
            return cpf
        except ValueError:
            print("CPF inválido. preencha novamente, por favor.")
