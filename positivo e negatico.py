n = int(input('Digite um Numeros: '))

if n == 0:
    classificacao = 'O numeros e 0'
elif n >=0:
    classificacao = 'O numeros positivo'
else:
    classificacao = 'O numeros e negarivo'
    
print(f"Classificação etária: {classificacao}")