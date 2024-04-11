menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
saque = 0
limite = 500
extrato = ""
number_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = input("Qual valor deseja depositar ? ")
        deposito = float(deposito)

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(saldo)

        else:
            print("Não pode ser depositado valores negativos")
    
    elif opcao == 's':

        if LIMITE_SAQUES >= 1 and saldo >= saque and saque < limite and saque >= 0:
            saque = input("Qual valor deseja sacar ? ")
            saque = float(saque)
            saldo = saldo - saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("Saque feito com sucesso!")
            print("Saldo Atual:", saldo)
            LIMITE_SAQUES -= 1
            
        else:
            print("Operação falhou, tente novamente!")
    
    elif opcao == 'e':
        print("============EXTRATO============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
    
    elif opcao == 'q':
        print("Agradecido!")
        break

    else:
        print("Operação inválida, por favor, selecione novamente")