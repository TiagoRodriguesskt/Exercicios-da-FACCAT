"""
Escreva um script para ler o número total de eleitores de um municipio, o número de votos brancos, nulos e validos.
Calcular e escrever o percentual que cada um representa no total de eleitores.
"""

try:
    eleitores_municipio = float(input("Digite o número de eleitores do municipio: "))
    votos_brancos = float(input("Digite o número de votos brancos: "))
    votos_nulos = float(input("Digite o números de votos nulos: "))
    votos_validos = float(input("Digite o número de votos validos: "))
except ValueError:
    print("Execute novamente e digite apenas numeros.")
    exit()

soma_votos = votos_brancos + votos_nulos + votos_validos
if soma_votos > eleitores_municipio:
    print("O total de votos nao pode ser maior que o total de eleitores.")
    exit()

porcetagem_brancos = (votos_brancos / eleitores_municipio) * 100
porcetagem_nulos = (votos_nulos / eleitores_municipio) * 100
porcetagem_validos = (votos_validos / eleitores_municipio) * 100
resultado = ((eleitores_municipio - soma_votos) / eleitores_municipio) * 100


print(f"A porcetagem de votos valiods é {porcetagem_validos:.2f}%.")
print(f"A porcetagem de votos nulos é {porcetagem_nulos:.2f}%.")
print(f"A porcetagem de votos brancos é {porcetagem_brancos:.2f}%.")
print(f" {resultado:.2f}")
