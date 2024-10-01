def soma(x,y):
    return x + y

def subritacao(x,y):
    return x - y

def divisao(x,y):
    if y !=0:
        return x / y
    else:
        return "Erro! Divisão por zero."


def mutipicacao(x,y):
    return x * y

# Exibir o menu
def menu():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Digite a operação (1/2/3/4) ou '5' para encerrar: ")
        
        if escolha == '5':
            print("Encerrando a calculadora...")
            break
        
        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print(f"O resultado é: {soma(num1, num2)}")
            elif escolha == '2':
                print(f"O resultado é: {subritacao(num1, num2)}")
            elif escolha == '3':
                print(f"O resultado é: {mutipicacao(num1, num2)}")
            elif escolha == '4':
                print(f"O resultado é: {divisao(num1, num2)}")
        else:
            print("Opção inválida. Tente novamente.")

        
    
calculadora()
        
