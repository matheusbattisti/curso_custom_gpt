
# Cálculo da média de uma lista de números

def calcular_media(numeros):
    soma = sum(numeros)
    count = len(numeros)
    media = soma / count
    return media

numeros = [10, 20, 30, 40, 50]
print("A média é:", calcular_media(numeros))
