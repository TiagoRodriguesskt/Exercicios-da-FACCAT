"""
Faça um script que pergunte qianto a pessoa ganha por hora (salário por hora) e o número
de horas trabalhadas no mês. Calcule e mostre o total do salário no mês.
"""

salario = float(input("Digite o salário por hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_mensal = salario * horas
print(f"O salário mensal é: {salario_mensal}")
