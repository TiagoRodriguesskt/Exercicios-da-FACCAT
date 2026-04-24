"""
Escreva um script que ler as dimessões de um retangulo(base e altura), calcule e escreva a área do retangulo.

Se você utilzar A = b x h, vai calcular a área do retangulo.
Se você utilzar A = b x h / 2, vai calcular a área do triangulo.
"""

base = float(input("Digite o valor da base do retangulo: "))
altura = float(input("Digite o valor da altura do retangulo:"))

area_retangulo = base * altura
area_triangulo = base * altura / 2
print(f"A área do retangulo é: {area_retangulo}")
print(f"A área do triangulo é: {area_triangulo}")
