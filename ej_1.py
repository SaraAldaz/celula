def lmatriz (n,m):
    matriz = []
    for i in range (n):
        while True:
            try:
                fila = list (map(int, input().split()))
                if len(fila) != m:
                    raise ValueError(f"Error: La fila {i+1} debe tener {m} elementos")
                matriz.append(fila)
                break
            except ValueError as e:
                print(e)
                print("Ingrese la fila correctamente")
    return matriz
def suma(a,b,n,m):
    c = [[a[i][j]+b[i][j] for j in range(m)] for i in range(n)]
    return c
try:
    n,m = (map(int, input("Ingrese size de la matriz: ").split()))
    if n <= 0 or m <=0:
        raise ValueError("Error N y M deben ser mayores a 0")
    print("Ingrese matriz A ")
    a = lmatriz(n,m)
    print("Ingrese matriz B")
    b = lmatriz(n,m)
    c = suma(a,b,n,m)
    print("Matriz resultado de la suma:")
    for fila in c:
        print(" ".join(map(str,fila)))
except ValueError as e:
    print (e)