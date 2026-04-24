"""
Escreva um script que analise o algoritmo abaixo e escreva o que será impresso na saída:
São 6 mesas de exercícios, cada mesa tem um algoritmo diferente.
"""


print("Mesa (a)")
A = 10
B = 20
# Valores iniciais
print(A, B)
# Valor de B alterado
B = 5
# Valor de A alterado
A = 2
print(A, B)

print("-" * 20)

# Mesa (b)
print("Mesa (b)")
A = 30
B = 20
C = A + B
print(C)
B = 10
print(B, C)
C = A + B
print(A, B, C)

print("-" * 20)

print("Mesa (c)")
A = 10
B = 20
C = A
B = C
A = B
print(A, B, C)


print("-" * 20)

print("Mesa (d)")
A = 10
B = A + 1
A = B + 1
B = A + 1
print(A)
A = B + 1
print(A, B)

print("-" * 20)

print("Mesa (e)")
A = 10
B = 5
C = A + B
B = 20
A = 10
print(A, B, C)

print("-" * 20)

print("Mesa (f)")
X = 1
Y = 2
Z = Y - X
print(Z)
X = 5
Y = X + Z
print(X, Y, Z)
