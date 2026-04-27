"""
Escreva um script para calcular e imprimir o número de lâmpadas que serão necessárias para iluminar
um determinado cômodo de um casa. Dados de entrada: a pontência da lâmpada utilizda (em watts),
as dimessões (largura e comprimnento, em metros) do cômodo. Considere que a
pontência necessaria é de 18 watts por metro quadrado.
"""

largura = float(input("Digite a largura do cômodo: "))
comprimeto = float(input("Digite o comprimento do cômodo: "))
potencia = float(input("Digite a potência da lâmpada: "))

area = largura * comprimeto
pontencia_necessaria = area * 18
lampadas = pontencia_necessaria / potencia

print(f"A area do cômodo é {area:.2f} metros quadrados.")
print(f"A quantidade necessárisa são {pontencia_necessaria:.2f} watts.")
print(f"São necessárias {lampadas:.1f} lâmpadas.")
