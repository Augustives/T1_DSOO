from controle.abstract_controlador_aluguel import AbstractControladorAluguel
from entidade.aluguel import Aluguel
from entidade.cadastro_duplicado_exception import CadastroDuplicadoException


class ControladorAluguel(AbstractControladorAluguel):
    from controle.controlador_principal import ControladorPrincipal

    def __init__(self, controlador_principal: ControladorPrincipal):
        from limite.tela_aluguel import TelaAluguel
        from controle.controlador_pessoa import ControladorPessoa
        from controle.controlador_quadra import ControladorQuadra
        super().__init__()
        self.__tela_aluguel = TelaAluguel(self)
        self.__lista_alugueis = list()
        self.__controlador_principal = controlador_principal
        self.__controlador_quadra = ControladorQuadra(self)
        self.__controlador_pessoa = ControladorPessoa(self)

    def inicia(self):
        self.abre_tela_aluguel()

    def abre_tela_aluguel(self):
        escolhas = {1: self.add_aluguel, 2: self.remove_aluguel,
                    3: self.lista_aluguel_mes, 4: self.lista_aluguel_dia,
                    0: self.voltar}  # precisa colocar as escolhas
        escolha = self.__tela_aluguel.mostra_opcoes()+
        funcao_escolhida = escolhas[escolha]
        funcao_escolhida()

    # não tá perfeito ainda
    def add_aluguel(self):
        identificador, cpf, dia, mes, hora = self.__tela_aluguel.tela_add_aluguel()
        #DA ONDE VEM OS CONTROLADORES ? DO ONTROLADOR PRINCIPAL ?
        quadra = self.__controlador_quadra.encontra_quadra(identificador)
        pessoa = self.__controlador_pessoa.encontra_pessoa(cpf)
        try:
            for aluguel in self.__lista_alugueis:
                if (aluguel.quadra == quadra and
                   aluguel.dia == dia and aluguel.mes == mes and aluguel.hora+1 > hora ):
                    raise CadastroDuplicadoException
        except CadastroDuplicadoException:
            print("Aluguel indisponível no horário desejado.")
            self.abre_tela_aluguel()

        aluguel_marcado = Aluguel(pessoa, quadra, dia, mes, hora)
        self.__lista_alugueis.append(aluguel_marcado)
        print("Aluguel cadastrado com sucesso.")
        self.recibo(pessoa.nome, pessoa.cpf,
                    quadra.esporte, dia, mes, hora)
        self.abre_tela_aluguel()

    def remove_aluguel(self):
        identificador, dia, mes, hora = self.__tela_aluguel.tela_remove_aluguel()
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
                print(aluguel.dia,"/", aluguel.mes,"/", aluguel.hora)

    def lista_aluguel_dia(self):
        dia = self.__tela_aluguel.tela_lista_aluguel_dia()
        for aluguel in self.__lista_alugueis:
            if aluguel.dia == dia:
                print("-"*30)
                print(aluguel.pessoa.nome)
                print(aluguel.pessoa.cpf)
                print(aluguel.quadra.identificador)
                print(aluguel.dia,"/", aluguel.mes,"às", aluguel.hora, "horas")

    def voltar(self):
        self.__controlador_principal.inicia()

    def recibo(self, nome: str, cpf: str,
                     esporte: str, dia: int,
                     mes: int, horario: int):
        self.__tela_aluguel.tela_recibo(nome, cpf, esporte, dia,
                                        mes, horario)
        self.abre_tela_aluguel()







