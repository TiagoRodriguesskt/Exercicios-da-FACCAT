"""
Esvreva um script para ler o salário mensal atual de um funcionário e o porcentagem de reajuste.
Calcular e escrever o novo salário.
"""

salario = float(input("Digite seu salario atual: "))
reajuste = float(input("Digite o novo reajuste salarial: "))

novo_salario = salario + (salario * reajuste / 100)
print(f"Seu salario foi de {salario} para {novo_salario} com reajuste de {reajuste}%")
