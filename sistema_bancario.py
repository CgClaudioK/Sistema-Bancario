import re
def menu():
    menu = """    
    Selecione a Opção desejada
    ===================
    [c] -> Cadastro novo user
    [n] -> Criar CC
    [lc]-> Listar CC
    [d] -> Depósito
    [s] -> Saque
    [e] -> Extrato
    [q] -> Quit
    

    ====================
            
            ==>"""
    return input(menu)


def deposito(saldo_atual, valor_deposito):
    if valor_deposito > 0:
        print("Deposito realizado com sucesso no valor de:" , valor_deposito)
        saldo_atual += valor_deposito
        extrato_atualizado = f"Depósito de: R${valor_deposito:.2f}\n"
    else: 
        print("Depósito com valores incorretos, tente novamente")
        print("Saldo atual de: R$", saldo_atual)
        extrato_atualizado = ""

    return saldo_atual, extrato_atualizado

def saque(saldo_atual, LIMITE_SAQUES, num_saque_diario, valor_saque):
    saques = num_saque_diario >= LIMITE_SAQUES
    if valor_saque > saldo_atual:
        print("Saldo Insuficiente para efetuar o saque")
        extrato_atualizado = ""
    elif valor_saque > LIMITE_SAQUES:
        print("Limite para saque insuficiente!")
        extrato_atualizado = ""
    elif saques:
        print("Limite diário de saques excedido")
        extrato_atualizado = ""
    elif valor_saque > 0:
        saldo_atual -= valor_saque
        print(f"Saque no valor de: R${valor_saque:.2f} efetuado com sucesso\n")
        extrato_atualizado = f"Saque de: R${valor_saque:.2f}\n"
        num_saque_diario += 1
    else:
        print("Operação falhou, tente novamente")
        extrato_atualizado = ""

    return saldo_atual, num_saque_diario, extrato_atualizado

def extrato(saldo_atual, extrato_atual):
    print( "=======EXTRATO BANCÁRIO SICREDI========\n")
    print( "Extrato detalhado:\n", extrato_atual)
    print(f"Saldo em conta: R${saldo_atual:.2f}\n")
    print( "=======================================")

#senti muita dificuldade em validar o usuario, eu consegui cadastrar mas não validar o CPF e me baseei no código da Trilha

def cadastro_usuarios(lista_usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = validar(cpf, lista_usuarios)

    if usuario:
        print("\nJá possui usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero, bairro, cidade/sigla estado): ")

    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def validar(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(AGENCIA, numero_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = validar(cpf, lista_usuarios)
    if usuario:
        print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}")

        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print (linha)

def main():
    contas = []
    saldo = 0
    limite = 500
    operacao = 0
    numero_saque_diario = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    extrato_atual = ""
    lista_usuarios = []
    while True:

        opcao = menu()

        if opcao == "d": 
            deposito_valor = float(input("Insira o Valor que você deseja depositar:"))
            saldo, extrato_atual = deposito(saldo, deposito_valor)
        
        elif opcao == "s": 
            saque_valor = float(input("Insira o Valor que você deseja sacar:"))
            saldo, numero_saque_diario, extrato_atual = saque(saldo, limite, numero_saque_diario, saque_valor)
            
        elif opcao == "e": 
            extrato(saldo, extrato_atual)

        elif opcao == "c":
            cadastro_usuarios(lista_usuarios)

        elif opcao == "n":
             numero_conta = len(contas) + 1
             conta = nova_conta(AGENCIA, numero_conta, lista_usuarios)
             if conta:
                contas.append(conta)
             

        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print("Quit")
            break

        else: 
            print("Opção escolhida é inválida, tente novamente")

main()