"""
Escreva um script para ler o raio de um circulo e calcular e escrever o valor da sua área.
Formula de um circulo:
piR^2
"""

from math import pi

area = float(input("Digite o raio do circulo:"))

area_circulo = pi * area**2
print(f"A area do circulo é {area_circulo:.2f}")
