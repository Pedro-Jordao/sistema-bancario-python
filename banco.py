menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

"""
Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

1500.45 = R$ 1500.45

Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir
uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação
de extrato.

"""
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    print("\n" + "=" * 30)
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor a ser depositado: R$ "))
        except ValueError:
            print("Valor inválido. Por favor, informe um número.")
            continue
        if valor > 0:
            saldo += valor
            extrato.append(f"+ R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito. Por favor, informe um valor positivo.")


    elif opcao == "s":
        try:
            valor = float(input("Informe o valor a ser sacado: R$ "))
        except ValueError:
            print("Valor inválido. Por favor, informe um número.")
            continue
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > limite:
            print(f"O valor do Saque não pôde ser realizado de acordo com o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido. Você já realizou {numero_saques} saques hoje.")
        else:
            saldo -= valor
            extrato.append(f"- R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "e":
        if not extrato:
            print("Não foi realizada nenhuma transação hoje.")
        else:
            print("Extrato: ")
            for transacao in extrato:
                print(transacao)
            print(f"Saldo atual: R$ {saldo:.2f}")
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
