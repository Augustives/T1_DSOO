class CadastroDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Cadastro Duplicado.")
