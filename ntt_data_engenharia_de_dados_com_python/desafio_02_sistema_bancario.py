def deposito(valor, saldo, extrato, /):
#"/": garante chamadas apenas por posição
    mensagem = ""
    retorno = ""

    if valor > 0:
        saldo += valor
        mensagem += f"+ Depósito: R$ {valor:.2f}\n"
        extrato += mensagem
        retorno = f"OPERAÇÃO REALIZADA:\n{mensagem}Saldo: R${saldo:.2f}"
    else:
        retorno = "OPERAÇÃO FALHOU:\nValor informado inválido! Tente novamente.\n"

    return retorno, saldo, extrato


def saque(*, valor, saldo, extrato, limite, numero_saques, limite_saques):
#"*": garante chamadas apenas por nome
    mensagem = ""
    retorno = ""

    if numero_saques == LIMITE_SAQUES:
        retorno = "OPERAÇÃO FALHOU:\nO total de 3 saques diários foi atingido!\n"
    elif valor > limite:
        retorno = f"OPERAÇÃO FALHOU:\nSeu limite por saque é de: {limite:.2f}\n"
    elif valor <= saldo:
        saldo -= valor
        mensagem = f"- Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        extrato += mensagem
        retorno = f"OPERAÇÃO REALIZADA:\n{mensagem}Saldo: R${saldo:.2f}"
    else:
        retorno = f"OPERAÇÃO FALHOU: Valor informado excede seu saldo de {saldo:.2f}\n"
    
    return retorno, saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    if extrato == "Seu extrato do período:\n":
        return "Nenhuma operação realizada no período."
    else:
        return extrato+f"Saldo: R${saldo:.2f}"


def existe_usuario(cpf):
    global usuarios

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            return True
        else:
            return False


def novo_usuario(cpf):
    global usuarios
    
    if existe_usuario(cpf):
        return f"CPF \"{cpf}\" já cadastrado!"
    else:
        nome = input("Informe seu nome completo: ")
        dt_nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
        endereco = input("Informe seu endereço (Logradouro, nº - Bairro - Cidade/UF): ")

        usuarios.append({"cpf":cpf, "nome":nome, "dt_nascimento":dt_nascimento, "endereco":endereco})

        return "Usuário cadastrado com sucesso!"
    

def nova_conta(cpf):
    global AGENCIA, contas, usuarios
    numero_conta = len(contas)+1
    
    if existe_usuario(cpf):
        contas.append({"cpf":cpf, "agencia":AGENCIA, "conta":numero_conta})
        return f"Conta Corrente AG:{AGENCIA} CC:{numero_conta} criada com sucesso!"
    else:
        return f"Usuário com CPF \"{cpf}\" não encontrado!"

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo Usuário
[c] Nova Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = "Seu extrato do período:\n"
numero_saques = 0
LIMITE_SAQUES = 3

retorno = ""
usuarios = []   #usar globalmente
AGENCIA = "0001"
contas = []     #usar globalmente

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        retorno, saldo, extrato = deposito(valor, saldo, extrato)
        print(retorno)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        retorno, saldo, extrato = saque (valor=valor
                                        ,saldo=saldo
                                        ,extrato=extrato
                                        ,limite=limite
                                        ,numero_saques=numero_saques
                                        ,limite_saques=LIMITE_SAQUES
                                        )
        print(retorno)
    elif opcao == "e":
        print(mostrar_extrato(saldo, extrato=extrato))
    elif opcao == "u":
        print(novo_usuario(input("Informe o CPF (apenas números): ")))
    elif opcao == "c":
        print(nova_conta(input("Informe o CPF do usuário: ")))
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")