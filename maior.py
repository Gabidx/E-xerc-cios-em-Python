while True:
    try:
        n1 = int(input('digite um numero:'))
        n2 = int(input('digite um numero:'))
        break
    except:
        print('Por favor digite o Numero inteiro')
    
def maior():    
    if (n1 == n2):
        print('Os dois numeros são iquais')
    elif n1 <= n2:
        print('O valor e Maior')
    elif n1 >= n2:
        print('O valor e Menor')
        
maior()
