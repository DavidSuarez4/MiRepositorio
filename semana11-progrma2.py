def ordenar (matriz, fila):
    n = len(matriz[0])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# La segunda fila esta desordenada
matrizDesordenada = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

# Mostrar matriz original
print("Matriz Desordenada:")
for fila in matrizDesordenada:
    print(fila)

# Ordenar una fila especfica de la matriz
ordenar(matrizDesordenada, 1)


print("Matriz Ordenada:")
for fila in matrizDesordenada:
    print(fila)