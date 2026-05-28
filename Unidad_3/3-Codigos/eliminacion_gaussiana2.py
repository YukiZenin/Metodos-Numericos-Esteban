def eliminacion_gaussiana():
    print("========================================")
    print("    MÉTODO DE ELIMINACIÓN GAUSSIANA     ")
    print("========================================")
    
    # 1. Solicitar el tamaño del sistema
    n = int(input("Ingrese el número de variables (ecuaciones): "))
    
    # 2. Lectura de datos
    matriz = []
    print("\nIngrese los coeficientes de la matriz aumentada fila por fila.")
    print("Separe los números con un espacio. Ejemplo: 2 1 -1 8")
    
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

    # 3. Eliminación hacia adelante (Triangulación)
    for i in range(n):
        # Pivoteo parcial: buscar el valor máximo en la columna actual
        max_fila = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[max_fila][i]):
                max_fila = k
        
        # Intercambiar filas si es necesario
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]
        
        # Validar si el pivote es cero
        if abs(matriz[i][i]) < 1e-9:
            print("\n⚠️ El sistema no tiene una solución única (pivote igual o cercano a cero).")
            return

        # Hacer ceros únicamente debajo del pivote actual
        for k in range(i + 1, n):
            factor = matriz[k][i] / matriz[i][i]
            for j in range(i, n + 1):
                matriz[k][j] -= factor * matriz[i][j]

    # Mostrar la matriz en su forma triangular superior
    print("\n========================================")
    print("      MATRIZ TRIANGULAR SUPERIOR        ")
    print("========================================")
    for fila in matriz:
        print([round(num, 4) for num in fila])

    # 4. Sustitución hacia atrás (Back-substitution)
    x = [0.0] * n
    # Empezamos desde la última ecuación hasta la primera
    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += matriz[i][j] * x[j]
        
        # Despejar la variable actual
        x[i] = (matriz[i][n] - suma) / matriz[i][i]

    # 5. Mostrar resultados finales
    print("\n========================================")
    print("          SOLUCIÓN DEL SISTEMA          ")
    print("========================================")
    for i in range(n):
        print(f"X{i+1} = {round(x[i], 4)}")

if __name__ == "__main__":
    eliminacion_gaussiana()
