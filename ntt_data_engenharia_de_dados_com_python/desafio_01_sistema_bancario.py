menu = " ESCOLHA UMA OPERAÇÃO ".center(50,"#")
menu += """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""
saldo = 0
limite = 500
extrato = "Seu extrato do período:\n"
numero_saques = 0
LIMITE_SAQUES = 3


def deposito(valor):
    global saldo, extrato
    mensagem = ""
    retorno = ""

    if valor > 0:
        print("aqui")
        saldo += valor
        mensagem += f"+ Depósito: R$ {valor:.2f}\n"
        extrato += mensagem
        retorno = f"OPERAÇÃO REALIZADA:\n{mensagem}Saldo: R${saldo:.2f}"
    else:
        retorno = "OPERAÇÃO FALHOU:\nValor informado inválido! Tente novamente.\n"

    return retorno


def saque(valor):
    global saldo, extrato, numero_saques, limite, LIMITE_SAQUES
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
    
    return retorno


while True:
    opcao = input(menu)

    if opcao == "d":
        #Tratar exceção ValueError
        print(deposito(float(input("Informe o valor do depósito: "))))
    elif opcao == "s":
        #Tratar exceção ValueError
        print(saque(float(input("Informe o valor do saque: "))))
    elif opcao == "e":
        if extrato == "Seu extrato do período:\n":
            print("Nenhuma operação realizada no período.")
        else:
            print(extrato+f"Saldo: R${saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, tente novamente!")
    
    
print(" OPERAÇÃO ENCERRADA! ".center(50,"#"))
print(" Obrigado por usar nosso sistema! ".center(50,"-"))