def buscar_valor(matriz, valor):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:

                return f"El valor {valor} se encontró en la posición ({i}, {j}) de la matriz."
    return f"El valor {valor} no se encontró en la matriz."

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

valorBuscar = 10

resultado = buscar_valor(matriz, valorBuscar)

print(resultado)