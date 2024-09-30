import textwrap
from abc import ABC, abstractmethod
    #, abstractclassmethod, abstractproperty #DESCONTINUADOS


##### VERSAO 01 - INI #####
class Transacao(ABC):
    '''
    def __init__(self):
        transacao = 0

    def registrar(self, conta):
        self.conta = conta
        transacao += 1
    '''

    @property
    @abstractmethod #ENTENDER MELHOR
    def get_valor(self):
        pass

    @classmethod  #ENTENDER MELHOR
    def registrar(self, conta):
        pass


#REVISTO - OK
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def get_valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.get_valor):
            conta.get_historico.adicionar_transacao(self)


#REVISTO - OK
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def get_valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.get_valor):
            conta.get_historico.adicionar_transacao(self)


#REVISTO - OK... troquei o insert por append
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


#REVISTO - OK.
class PessoaFisica(Cliente):
    def __init__(self,cpf,nome,data_nascimento,endereco):
        super().__init__(endereco)  #instanciando novo cliente e herdando
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


#COPIADO - OK
class Historico:
    def __init__(self):
        self.transacoes = []

    #COPIEI, NÂO SOUBE FAZER
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            #Armazena a info na lista, como um dicionário
            {  "tipo": transacao.__class__.__name__
             , "valor": transacao.get_valor
             #, "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
             ,
            }
        )


#REVISTO - OK
class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._cliente = cliente
        self._numero = numero
        self._historico = Historico()

    #Banco digital apenas com uma agencia
    def agencia_padrao(self):
        return '0001'

    @classmethod
    def nova_conta(cls, cliente, numero):
        #RETORNA UMA INSTANCIA DE CONTA
        return cls(cliente, numero)
    
    #ABAIXO AS PROPRIEDADES PARA QUE OS VALORES DOS ATRIBUTOS PRIVADOS SEJAM ACESSADOS
    @property
    def saldo(self):    #PODERIA SER get_saldo(), mas paor conta da UML, mantive saldo()
        return self._saldo
    @property
    def get_numero(self):
        return self._numero
    @property
    def get_agencia(self):
        return self.agencia_padrao()
    @property
    def get_cliente(self):
        return self._cliente
    @property
    def get_historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("\nOPERAÇÃO FALHOU! Valor solicitado excede seu saldo.")
            return False
        elif valor <= 0:
            print("\nOPERAÇÃO FALHOU! Valor solicitado deve ser maior que zero.")
            return False
        else:
            self._saldo -= valor
            print(f"\nOPERAÇÃO REALIZADA: Saque no valor de R${valor:.2f}!")
            return True
        
    def depositar(self, valor):
        if valor <= 0:
            print("\nOPERAÇÃO FALHOU! Valor depositado deve ser maior que zero.")
            return False
        else:
            self._saldo += valor
            print(f"\nOPERAÇÃO REALIZADA: Depósito no valor de R${valor:.2f}!")
            return True
            

#REVISTO - OK
class ContaCorrente(Conta):
    '''
    #ERRADO colocar aqui
       , pois as variáveis são compartilhadas por todos os objetos
    
    _numero_saques_feitos = 0
    _valor_saques_feitos = 0
    '''

    def __init__(self, cliente, numero, limite = 500, limite_saques = 3):
        super().__init__(cliente, numero)
        self._limite = limite
        self._limite_saques = limite_saques

    #No curso sobrescreveram, para fazer novos tratamentos,
    #poderiam ter sido feitos na classe pai, porém pela uml faz sentido fazer aqui
    def sacar(self,valor):
        #COPIEI, NÂO SOUBE FAZER
        saques_realizados = len([transacao for transacao in self.get_historico.transacoes if transacao["tipo"] == "Saque"])

        if saques_realizados >= self._limite_saques:
            print(f"\nOPERAÇÃO FALHOU: O total de {self._limite_saques} saques diários foi atingido!")
            return False            
        elif valor > self._limite:
            print(f"\nOPERAÇÃO FALHOU: Seu limite por saque é de: {self._limite:.2f}")
            return False
        else:
            return super().sacar(valor)
        
    #COPIADO, representação da minha agencia e conta
    def __str__(self):
        return f"""\
            Agência:\t{self.get_agencia}
            Conta:\t\t{self.get_numero}
            Titular:\t{self.get_cliente.nome}
        """

##### VERSAO 01 - FIM #####


##### VERSAO 02 - INI #####
#####   COPIADA E AJUSTADA    #####

def filtrar_cliente(cpf, clientes):
    cliente_filtrado = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente_filtrado[0] if cliente_filtrado else None
        #havia esquecido de indicar o index da lista cliente_filtrado


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui contas cadastradas!")
        return
    
    #FIXME: AINDA NÂO PERMITE QUE O CLIENTE ESCOLHA A CONTA
    return cliente.contas[0]


def deposito(clientes):
    cpf = input("\nInforme o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    transacao = Deposito(float(input("Informe o valor do depósito: ")))
    conta = recuperar_conta_cliente(cliente)
    
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def saque(clientes):
    cpf = input("\nInforme o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    transacao = Saque(float(input("Informe o valor do saque: ")))
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def mostrar_extrato(clientes):
    cpf = input("\nInforme o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n" + str.center(" EXTRATO ",25,"="))
    extrato = ""

    transacoes = conta.get_historico.transacoes
    if not transacoes:
        extrato += "\nSem movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\tR${transacao['valor']:.2f}"

    extrato += f"\SALDO:\tR$ {conta.saldo:.2f}"
    
    print("-"*25)
    print(extrato)
    print("="*25)


def novo_usuario(clientes):
    cpf = input("\nInforme o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if  cliente:
        print("\nCliente já cadastrado!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
    endereco = input("Informe seu endereço (Logradouro, nº - Bairro - Cidade/UF): ")

    cliente = PessoaFisica(cpf=cpf,nome=nome,data_nascimento=data_nascimento,endereco=endereco)
    clientes.append(cliente)

    print("\nCliente criado com sucesso!")


def nova_conta(numero, clientes, contas):
    cpf = input("\nInforme o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))
    

def main():
    lista_clientes = []
    lista_contas = []

    menu = "\n" + str.center(" MENU ",50,"=") + """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Novo Usuário
    [c] Nova Conta
    [l] Lista Contas
    [q] Sair
    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            deposito(lista_clientes)
        elif opcao == "s":
            saque(lista_clientes)
        elif opcao == "e":
            mostrar_extrato(lista_clientes)
        elif opcao == "u":
            novo_usuario(lista_clientes)
        elif opcao == "c":
            nova_conta(len(lista_contas)+1,lista_clientes,lista_contas)
        elif opcao == "l":
            listar_contas(lista_contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")



main()