menu = """

========-Menu-=========

[1] Depositar
[2] Saque
[3] Extrato
[0] Sair

========-Fim Menu-======
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
  opcao = input(menu)

  if opcao == "1":
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação não realizada! O valor informado é invalido.")

  elif opcao == "2":
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
       print("Operação não realizada! Você não tem saldo suficiente na conta.")

    elif excedeu_limite:
       print("Operação não realizada! Numero de saques excedido.")

    elif excedeu_saques:
       print("Operação não realizada! Quantidade maxima de saques excedidas.")

    elif valor > 0:
       saldo -= valor
       extrato += f"Saque: R$ {valor:.2f}\n"
       numero_saques += 1

    else:
       print("Operação não realizada! O Valor informado é invalido.")

  elif opcao == "3":
     print("\n=============== Extrato ===============")
     print("Ainda não há movimentações na conta." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("=========================================")

  elif opcao == "0":
     print("Obrigado por usar nossos serviços. Até logo!")
     break
  
  else:
     print("Opração invalida, Selecione uma opração válida no Menu.")
  

    

