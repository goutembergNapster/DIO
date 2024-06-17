menu = """

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Deposito")
        valor_deposito = float(input("Digite o valor desejado: "))
        if valor_deposito < 0:
            print("Valor inválido, depositos não podem ser menores que zero!")

        else:
            print(f"Deposito de R$ {valor_deposito} Reais Realizado com sucesso")
            saldo = saldo + valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f} (+) \n"

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Digite o valor do saque: "))

        limite_saque = numero_saques >= LIMITE_SAQUE

        if valor_saque > saldo:
            print("Saldo insuficiente para saque")
        elif valor_saque > limite:
            print(f"O limite de saque é R$ {limite} Reais ")
        elif limite_saque:
            print("Você excedeu o limite diário para saques")
        else:
            print("Saque Realizado com sucesso")
            saldo = saldo - valor_saque
            print(f"Seu novo saldo é RS {saldo} Reais")
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f} (-) \n"

    elif opcao == "e":
        print("\n##########Extrato Para Simples Conferencia##########")
        print("\n##########Os Valores Podem Sofrer Alterações##########")
        print("Sem movimentações de entrada ou de saída." if not extrato else extrato)
        print(f"\nSeu Saldo é: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")