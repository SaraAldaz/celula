def lmatriz (n):
    matriz = []
    for i in range (n):
        while True:
            try:
                fila = list (map(int, input().split()))
                if len(fila) != n:
                    raise ValueError(f"Error: La fila {i+1} debe tener {n} elementos")
                matriz.append(fila)
                break
            except ValueError as e:
                print(e)
                print("Ingrese la fila correctamente")
    return matriz
def rotar_90(matriz,n):
    transposicion = [[matriz[i][j]for j in range(n)]for i in range(n)]
    rotacion = [fila[::-1]for fila in transposicion]
    return rotacion
try:
    n = int(input("Ingrese size de la matriz: "))
    if n <= 0:
        raise ValueError("Error N debe ser mayor a 0")
    print("Ingrese matriz ")
    matriz = lmatriz(n)
    matrizr = rotar_90(matriz,n)
    for fila in matrizr:
        print(" ".join(map(str,fila)))
except ValueError as e:
    print (e)