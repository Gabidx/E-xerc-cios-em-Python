while True:
    try:
        numero1 = int(input('Digite a Primeira Nota:'))
        numero2 = int(input('Digite a Segunda Nota:'))
        numero3 = int(input('Digite a Terseira nota:'))
        
        break
    except:
        print('Por favor digite o Numero inteiro')
        
def media():
    media =(numero1 +numero2 + numero3) /3
    if media >=7 :
        print(f'Voce esta Aprovado sua media foi de {media}')
    else:
        print(f'Voce esta Reprovado sua media foi de {media}')
media()