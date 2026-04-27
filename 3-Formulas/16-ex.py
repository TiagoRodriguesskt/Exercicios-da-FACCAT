"""
Escreva um script que leia 3 notas de um aluno, clacule e escreva a média final desta.
Considere que a média é ponderada e que o peso das notas é 2, 3 e 5.
Formulapara o cálculo da média ponderada:

mediafinal = n1*2 + n2*3 + n3*5 / 10
"""

n1 = float(input("Digita a primeura nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota:"))

media_final = (n1 * 2 + n2 * 3 + n3 * 5) / 10

print(f"A media do aluno é {media_final:.2f}.")
