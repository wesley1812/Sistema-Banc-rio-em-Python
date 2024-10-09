saldo = 1200
quantidade_saques = 0
valores_depositos = []
valores_saques = []


def deposit(valor):
    global saldo
    saldo += valor 
    valores_depositos.append(valor)

    return saldo

def saque(valor):
    global saldo
    
    if valor > 500:
        print("Não será possível realizar o saque. Valor máximo permitido")
        saldo
    else:
        global quantidade_saques 
        if quantidade_saques < 3:
            saldo -= valor
            quantidade_saques += 1
        else:
            print("Não será possível realizar o saque. Quantidade máxima atingida")
            saldo
    valores_saques.append(valor)
    
    return saldo
    
def extrato():
    global saldo
    global valores_saques
    global valores_depositos

    print(f"""
        EXTRATO
        Seu depositos foram: {valores_depositos}
        Seus saques foram: {valores_saques}
        Seu saldo atual é: {saldo}
        """)

while True: 

    opçao = input("""
MENU
                  
1 - Depositar
2 - Sacar
3 - Ver extrato
4 - Sair
              
Olá, escolha sua opção: """)

    if opçao == "1":
        deposit(int(input("Digite o valor a ser depositado: R$")))
    elif opçao == "2":
        saque(int(input("Digite o valor a ser sacado: R$")))
    elif opçao == "3":
        extrato()
    elif opçao == "4":
        print("Saindo")
        break
    else:
        print("Digite uma opção válida")