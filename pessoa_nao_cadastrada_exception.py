class PessoaNaoCadastradaException(Exception):
    def __init__(self):
        super().__init__("O usuário desejado não possui cadastro.")
