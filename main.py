menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        palavra = "Depósito"
        print(palavra.center(20,"="))
        deposito = int(input(f"Digite o valor que você deseja depositar:\n"))
        if (deposito <= 0):
            print("Valor inválido, digite um valor válido!")
            input("Digite qualquer tecla para voltar:\n")
        elif (deposito > 0):
            saldo += deposito
            extrato.append(f"-Você realizou um deposito de: R${deposito}")
            print("Depostio realizado com sucesso!")
            input("Digite qualquer tecla para voltar:\n")
    
    elif opcao == "s":
        palavra = "Saque"
        print(palavra.center(20,"="))
        saque = int(input(f"Digite o valor que você deseja sacar:\n"))
        if (saque > saldo):
                print("Saldo insuficiente!")
                input("Digite qualquer tecla para voltar:\n")
        if (saque <= limite):
            if (numero_saques<LIMITE_SAQUES):
                saldo -= saque
                extrato.append(f"-Você realizou um saque de: R${saque}")
                print("Saque realizado com sucesso!")
                input("Digite qualquer tecla para voltar:\n")
                numero_saques += 1
            else:
                print("Você excedeu o limite de saques!")

    elif opcao == "e":
        palavra = "Extrato"
        print(palavra.center(20,"="))
        print(f"Seu saldo é de: {saldo}\n")
        print(f"{extrato}")
        input("Digite qualquer tecla para voltar:\n")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")