from abc import ABC, abstractmethod


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

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
