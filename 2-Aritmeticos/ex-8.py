"""
Escreva um script que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa
em dias. Considerar ano com 365 dias e mês com 30 dias.
Calcular quantos dias a pessoa já viveu.
EX.: 
- Idade: 10 anos, 12 meses e 30 dias
- Dias vividos: 4410 dias

Mas pode ser qualquer idade, meses e dias.
O correto seria considerar o dia do nascimento, mês e ano.
"""

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

dias = dia + (mes * 30) + (ano * 365)
print(f"A pessoa tem {dias} dias de vida vividos.")
