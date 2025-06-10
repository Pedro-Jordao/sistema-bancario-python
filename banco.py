menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta Corrente
[lc] Listar Contas
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

# Listas para armazenar usuários e contas
usuarios = []
contas = []


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f" R$ + {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito. Por favor, informe um valor positivo.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(f"O valor do Saque não pôde ser realizado de acordo com o limite de R$ {limite:.2f}.")
    elif numero_saques >= limite_saques:
        print(f"Limite de saques diários atingido. Você já realizou {numero_saques} saques hoje.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f" R$ - {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque. Por favor, informe um valor positivo.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\nExtrato:")
    if not extrato:
        print("Não foi realizada nenhuma transação hoje.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"Saldo atual: R$ {saldo:.2f}")


# Função para criar usuário

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")


# Função para criar conta corrente

def criar_conta_corrente(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}")


# Função para listar contas

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        usuario = conta['usuario']
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Usuário: {usuario['nome']} | CPF: {usuario['cpf']}")


while True:
    print("\n" + "=" * 30)
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor a ser depositado: R$ "))
        except ValueError:
            print("Valor inválido. Por favor, informe um número.")
            continue
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor a ser sacado: R$ "))
        except ValueError:
            print("Valor inválido. Por favor, informe um número.")
            continue
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        criar_conta_corrente(contas, usuarios)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
