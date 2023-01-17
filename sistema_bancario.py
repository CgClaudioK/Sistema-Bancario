menu = """    
 Selecione a Opção desejada
 ===================
  [d] -> Depósito
  [s] -> Saque
  [e] -> Extrato
  [q] -> Quit

  ====================
            
            ==>"""
saldo = 0
limite = 500
operacao = 0
numero_saque_diario = 0
LIMITE_SAQUES = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "d": 
       deposito =  float (input("Insira o Valor que você deseja depositar:"))
      
       if deposito > 0:
             print("Deposito realizado com sucesso no valor de:" , deposito)
             saldo += deposito
             extrato += f"Depósito de: R${deposito:.2f}\n"
       else: 
             print("Depósito com valores incorretos, tente novamente")
             print ("Saldo atual de: R$",saldo)
       
    elif opcao == "s": 
        saque =  float (input("Insira o Valor que você deseja sacar:"))
        saques = numero_saque_diario >=LIMITE_SAQUES

        if saque > saldo:
            print ("Saldo Insuficiente para efetuar o saque")
        elif saque > limite:
            print ("Limite para saque insuficiente!")
        elif saques:
            print("Limite diário de saques excedido")
        elif saque > 0: 
            saldo -= saque
            print (f"Saque no valor de: R${saque:.2f} efetuado com sucesso\n")
            extrato += f"Saque de: R${saque:.2f}\n"
            numero_saque_diario +=1
        else: 
            print("Operação falhou, tente novamente")
        
        
        

    elif opcao == "e": 
        print("=======EXTRATO BANCÁRIO SICREDI========\n")
        print("Extrato detalhado:\n", extrato )
        print(f"Saldo em conta: R${saldo:.2f}\n")
        print("=======================================")
        

    elif opcao == "q":
        print("Quit")
        break

    else: print("Opção escolhida é inválida, tente novamente")

