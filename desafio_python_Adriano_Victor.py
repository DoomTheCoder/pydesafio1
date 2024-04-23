menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
quantidade_de_saques_diarios_realizados = 0
historico_de_depositos = []
historico_de_saques = []

while True:

    opcao = input(menu)

    if opcao[-1].lower() == "d":
        print("Digite um valor para depósito")
        valor_deposito = float(input())
        if valor_deposito > 0:
            saldo += valor_deposito
            historico_de_depositos.append(valor_deposito)
            print(f" Seu saldo no valor de R${valor_deposito:.2f} foi depositado")
        else:
            print("Valor de depósito inválido, por favor, tente novamente")


    elif opcao[-1].lower() == "s":
        print("Digite um valor para saque, máximo R$500,00 por saque")
        valor_de_saque = float(input())
        if valor_de_saque <= limite and quantidade_de_saques_diarios_realizados < LIMITE_SAQUES:
            if saldo - valor_de_saque >= 0:
                saldo -= valor_de_saque
                historico_de_saques.append(valor_de_saque)
                quantidade_de_saques_diarios_realizados += 1
                print(f"Você sacou R${valor_de_saque:.2f} com sucesso!")
            else:
                print("Não foi possível realizar o saque, saldo insuficiente")
        else:
                print("operação inválida, limite de saques ou quantidade de saque acima do permitido, tente novamente")
        


    elif opcao == "e" or opcao[-1].lower() == "e":
        for item in historico_de_depositos:
            print(f"Seus depósitos recentes foram: R${item:.2f}" )
        for item in historico_de_saques:
            print(f"Seus saques recentes foram: R${item:.2f}")
        print(f"Seu saldo atual é: R${saldo:.2f}")


    elif opcao[-1].lower() == "q":
        print("Operação encerrada, obrigado por usar nosso sistema!")
        break
    
    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada!")