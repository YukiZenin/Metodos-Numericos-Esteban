def gauss_jordan():
    print("========================================")
    print("      MÉTODO DE GAUSS-JORDAN            ")
    print("========================================")
    
    # 1. Solicitar el tamaño del sistema
    n = int(input("Ingrese el número de variables (ecuaciones): "))
    
    # 2. Lectura de datos
    matriz = []
    print("\nIngrese los coeficientes de la matriz aumentada fila por fila.")
    print("Separe los números con un espacio. Ejemplo para '2x + 3y = 5' -> Ingrese: 2 3 5")
    
    for i in range(n):
        while True:
            try:
                fila = list(map(float, input(f"Fila {i+1}: ").split()))
                if len(fila) == n + 1:
                    matriz.append(fila)
                    break
                else:
                    print(f"❌ Error: Debes ingresar exactamente {n + 1} valores.")
            except ValueError:
                print("❌ Error: Ingrese solo números válidos.")

    # 3. Proceso Iterativo de Gauss-Jordan
    for i in range(n):
        # Pivoteo parcial: buscar el valor máximo en la columna actual para evitar divisiones por cero
        max_fila = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[max_fila][i]):
                max_fila = k
        
        # Intercambiar filas si es necesario
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]
        
        # Validar si el pivote es cero o muy cercano a cero
        if abs(matriz[i][i]) < 1e-9:
            print("\n⚠️ El sistema no tiene una solución única (pivote igual o cercano a cero).")
            return

        # Hacer que el pivote de la fila actual sea igual a 1
        pivote = matriz[i][i]
        for j in range(i, n + 1):
            matriz[i][j] /= pivote

        # Hacer cero los demás elementos de la columna 'i' (tanto arriba como abajo)
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(i, n + 1):
                    matriz[k][j] -= factor * matriz[i][j]

    # 4. Mostrar la matriz reducida y los resultados
    print("\n========================================")
    print("  MATRIZ ESCALONADA REDUCIDA (FINAL)    ")
    print("========================================")
    for fila in matriz:
        # Redondeamos a 4 decimales para una lectura limpia
        print([round(num, 4) for num in fila])

    print("\n========================================")
    print("          SOLUCIÓN DEL SISTEMA          ")
    print("========================================")
    for i in range(n):
        print(f"X{i+1} = {round(matriz[i][n], 4)}")

if __name__ == "__main__":
    gauss_jordan()
