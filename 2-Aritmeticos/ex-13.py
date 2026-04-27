"""
O custo de um carro novo ao consumidor é a soma do
custo de fábrica com a porcetagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Suponha que a porcetagem do distribuidor seja de 28% e os impostos de 45%.
Escreva um script que leia o custo de fábrica de um carro, calcule e escreva o custo final ao consumidor.
"""

carro = float(input("Digite o custo do carro de fábrica: "))

distribuindora = carro * 0.28
imposto = carro * 0.45

custo_final = carro + distribuindora + imposto

print(f"O custo do carro de fábrica foi de {carro:.3f}")
print(f"O custo da distribuidora foi de {distribuindora:.3f}")
print(f"O custo dos impostos foi de {imposto:.3f}")
print(f"O valor total do carro sai por {custo_final:.3f}")
