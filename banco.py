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
        print("Saque")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
