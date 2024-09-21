# Menu de seleção das funções disponíveis
menu = """
--------------
[0] Depositar
--------------
[1] Sacar
--------------
[2] Extrato
--------------
[3] Sair
--------------
=> """

# Saldo inicial ao executar programa
saldo = 0
# Valor máximo de saque permitido, por operação
limite = 500
# Valor inicial do extrato ao executar programa
extrato = ""
# Quantidade de saques efetuados inicialmente ao executar programa
numero_saques = 0
# Limite de saques permitido diariamente
LIMITE_SAQUES = 3

# Execução inicial do programa
while True:

    # Apresenta o menu inicial para seleção da operação desejada
    opcao = input(menu)

    # Seleção da opção de depósito
    if opcao == "0":
        valor = float(input("Informe o valor que deseja depositar:").replace(',', '.'))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação concluída com sucesso!")

        else:
            print("Operação não concluída! O valor informado não é válido.")

    # Seleção da opção de saque
    elif opcao == "1":
        valor = float(input("Informe o valor que deseja sacar: ").replace(',', '.'))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não concluída! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação não concluída! Valor do saque excedeu limite.")

        elif excedeu_saques:
            print("Operação não concluída! Número máximo de saques permitido no dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação concluída com sucesso!")

        else:
            print("Operação não concluída! O valor informado não é válido.")
    
    # Seleção da opção de extrato
    elif opcao == "2":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================")

    # Seleção da opção de sair
    elif opcao == "3":
        break

    # Condição para qualquer valor diferente das opções disponíveis
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
