def gauss_seidel():
    print("========================================")
    print("        MÉTODO DE GAUSS-SEIDEL          ")
    print("========================================")
    
    # 1. Solicitar el tamaño del sistema
    n = int(input("Ingrese el número de variables (ecuaciones): "))
    
    # 2. Lectura de la matriz aumentada
    A = []
    b = []
    print("\nIngrese los coeficientes de la matriz aumentada fila por fila.")
    print("Separe los números con un espacio. Ejemplo: 10 2 -1 27")
    
    for i in range(n):
        while True:
            try:
                fila = list(map(float, input(f"Fila {i+1}: ").split()))
                if len(fila) == n + 1:
                    A.append(fila[:n])  # Coeficientes
                    b.append(fila[n])   # Términos independientes
                    break
                else:
                    print(f"❌ Error: Debes ingresar exactamente {n + 1} valores.")
            except ValueError:
                print("❌ Error: Ingrese solo números válidos.")

    # 3. Parámetros del método iterativo
    tol = float(input("\nIngrese la tolerancia (ej. 0.0001): "))
    max_iter = int(input("Ingrese el número máximo de iteraciones (ej. 100): "))
    
    # Vector de aproximación inicial (empezamos en 0 para todas las variables)
    x = [0.0] * n
    
    # Validar que no haya ceros en la diagonal principal
    for i in range(n):
        if abs(A[i][i]) < 1e-9:
            print(f"\n⚠️ Error: El elemento en la diagonal A[{i+1}][{i+1}] es cero o muy cercano a cero.")
            print("El método de Gauss-Seidel no puede continuar sin reordenar las ecuaciones.")
            return

    print("\nComenzando iteraciones...")
    print(f"{'Iteración':<10} | {'Valores de X':<40} | {'Error Máximo':<15}")
    print("-" * 75)

    # 4. Proceso Iterativo
    for iteracion in range(1, max_iter + 1):
        x_anterior = list(x)  # Guardar los valores de la iteración pasada para calcular el error
        
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]  # Usa los valores más recientes de 'x'
            
            # Fórmula de Gauss-Seidel
            x[i] = (b[i] - suma) / A[i][i]
        
        # Calcular el error absoluto máximo entre la iteración actual y la anterior
        error = max(abs(x[i] - x_anterior[i]) for i in range(n))
        
        # Mostrar progreso de esta iteración
        valores_str = ", ".join([f"X{k+1}={round(val, 5)}" for k, val in enumerate(x)])
        print(f"{iteracion:<10} | {valores_str:<40} | {error:.6f}")
        
        # Condición de parada (si el error es menor que la tolerancia)
        if error < tol:
            print("\n✅ ¡El método convergió con éxito!")
            break
    else:
        print("\n⚠️ Se alcanzó el número máximo de iteraciones sin lograr la tolerancia requerida.")

    # 5. Mostrar resultados finales
    print("\n========================================")
    print("          SOLUCIÓN FINAL                ")
    print("========================================")
    for i in range(n):
        print(f"X{i+1} = {round(x[i], 5)}")

if __name__ == "__main__":
    gauss_seidel()
