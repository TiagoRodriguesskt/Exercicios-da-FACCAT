"""
Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
mais uma comissão fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas.
Escreva u  script fixo que leia o número de carros vendidos, o valor total de  suas vendas,
o salário fixo e o valor que ele recebe por carro vendido.m Calcule e escreva o valor
final do salário do vendedor.
"""

salario_fixo = float(input("Digite o salário fixo: "))
valor_por_carro = float(input("Quanto ele ganha por cada carro vendido? "))
qtd_carros = float(input("Quantos carros foram vendidos? "))
total_vendas = float(input("Digite o valor total das vendas: "))

bonus_carros = qtd_carros * valor_por_carro
comissao_vendas = total_vendas * 0.05

salario_final = salario_fixo + bonus_carros + comissao_vendas

print(f"O salário final do funcionário foi de R$ {salario_final:.2f}")

# Cálculo errado:
# salario_final = salario_fixo + (qtd_carros * valor_por_carro) + (total_vendas * 0.05)
# print(f"O salário final do funcionário foi de R$ {salario_final:.2f}")
