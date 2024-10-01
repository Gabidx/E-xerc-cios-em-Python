AnoDoNasimento = int(input('Digite o seu Ano de Nasimento: '))
Ano = 2024
idade = AnoDoNasimento - Ano

if idade <= 17:
    classificacao = 'E Menor De Idade'
else:
    classificacao = 'E Maior de Idade'

print(f"Classificação etária: {classificacao}")