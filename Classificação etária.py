idade = int(input('digite a idade: '))

if idade <=12:
    classificacao = 'uma Criança!'
elif idade <= 13:
    classificacao = 'Adolecente!'
elif idade <= 20:
    classificacao = 'Jovem!'
elif idade <= 40:
    classificacao = 'Adulto!'
elif idade <= 60:
    classificacao = ' Meia Idade!'
else:
    classificacao = 'Idoso'
    
print(f"Classificação etária: {classificacao}")
