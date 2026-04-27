"""
Escreva um script para ler uma temperatura em graus Fahrenheit e calcular e excrever o
valor correspondente em graus Celsius(baseado na formula abaixo).

C/5 = F-32/9

OBS.: Para testar nesse exercício, use o seguinte valor: 212°F = 100°C
"""

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fahrenheit - 32) / 9 * 5

if celsius < 0:
    print("A temperatura é negativa.")
elif celsius == 0:
    print("A temperatura é neutra.")
elif celsius > 0 and celsius <= 25:
    print("Temperatura agradavel.")
else:
    print("A temperatura está alta.")

print(f"A temperatura em Celsius é {celsius:.2f}.")
