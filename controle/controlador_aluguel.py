from controle.abstract_controlador_aluguel import AbstractControladorAluguel
from entidade.aluguel import Aluguel
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException


class ControladorAluguel(AbstractControladorAluguel):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_aluguel import TelaAluguel
        super().__init__()
        self.__tela_aluguel = TelaAluguel(self)
        self.__lista_alugueis = list()
        self.__controlador_principal = controlador_principal

    def inicia(self):
        self.abre_tela_aluguel()

    def abre_tela_aluguel(self):
        escolhas = {1: self.add_aluguel, 2: self.remove_aluguel,
                    3: self.lista_aluguel_mes, 4: self.lista_aluguel_dia,
                    0: self.voltar}
        escolha = self.__tela_aluguel.mostra_opcoes()
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()

    def add_aluguel(self):
        identificador, cpf, dia, mes, hora = self.__tela_aluguel.tela_add_aluguel()
        try:
            quadra = self.__controlador_principal.encontra_quadra(identificador)
            pessoa = self.__controlador_principal.encontra_pessoa(cpf)
            if quadra is None or pessoa is None:
                raise ValueError
            for aluguel in self.__lista_alugueis:
                if (aluguel.quadra == quadra and
                        aluguel.dia == dia and
                        aluguel.mes == mes and aluguel.hora+1 > hora):
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Aluguel indisponível no horário desejado.")
            self.abre_tela_aluguel()
        except ValueError:
            print("Quadra ou pessoa inexistentes.")
            self.abre_tela_aluguel()

        aluguel_marcado = Aluguel(pessoa, quadra, dia, mes, hora)
        self.__lista_alugueis.append(aluguel_marcado)
        print("Aluguel cadastrado com sucesso.")
        self.recibo(pessoa.nome, pessoa.cpf,
                    quadra.esporte, dia, mes, hora)
        self.abre_tela_aluguel()

    def remove_aluguel(self):
        identificador, dia, mes, hora = self.__tela_aluguel.tela_remove_aluguel()
        quadra = self.__controlador_principal.encontra_quadra(identificador)
        for aluguel in self.__lista_alugueis:
            if (aluguel.quadra == quadra and
                    aluguel.dia == dia and aluguel.mes == mes and aluguel.hora == hora):
                self.__lista_alugueis.remove(aluguel)
                print("Aluguel cancelado com sucesso.")
                self.abre_tela_aluguel()
        print("Aluguel inexistente.")
        self.abre_tela_aluguel()

    def lista_aluguel_mes(self):
        mes = self.__tela_aluguel.tela_lista_aluguel_mes()
        for aluguel in self.__lista_alugueis:
            if aluguel.mes == mes:
                print("-"*30)
                print(aluguel.pessoa.nome)
                print(aluguel.pessoa.cpf)
                print(aluguel.quadra.identificador)
                print(aluguel.dia, "/", aluguel.mes, "às",
                      aluguel.hora, "horas")

    def lista_aluguel_dia(self):
        dia = self.__tela_aluguel.tela_lista_aluguel_dia()
        for aluguel in self.__lista_alugueis:
            if aluguel.dia == dia:
                print("-"*30)
                print(aluguel.pessoa.nome)
                print(aluguel.pessoa.cpf)
                print(aluguel.quadra.identificador)
                print(aluguel.dia, "/", aluguel.mes, "às",
                      aluguel.hora, "horas")

    def voltar(self):
        self.__controlador_principal.inicia()

    def recibo(self, nome: str, cpf: str,
               esporte: str, dia: int,
               mes: int, horario: int):
        self.__tela_aluguel.tela_recibo(nome, cpf, esporte, dia,
                                        mes, horario)
        self.abre_tela_aluguel()
