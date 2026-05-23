def interpolacion_lineal():
    print("\n--- Interpolación Lineal ---")
    x0 = float(input("Ingresa x0: "))
    y0 = float(input("Ingresa y0: "))
    x1 = float(input("Ingresa x1: "))
    y1 = float(input("Ingresa y1: "))
    x_obj = float(input("¿Qué valor de x quieres encontrar?: "))
    
    if x1 == x0:
        return "Error: x1 y x0 no pueden ser iguales."
        
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x_obj - x0)
    return f"Resultado: Para x={x_obj}, el valor de y es {y}"

def interpolacion_cuadratica():
    print("\n--- Interpolación Cuadrática ---")
    x0 = float(input("Ingresa x0: "))
    y0 = float(input("Ingresa y0: "))
    x1 = float(input("Ingresa x1: "))
    y1 = float(input("Ingresa y1: "))
    x2 = float(input("Ingresa x2: "))
    y2 = float(input("Ingresa y2: "))
    x_obj = float(input("¿Qué valor de x quieres encontrar?: "))
    
    # Verificación para evitar división por cero
    if x0 == x1 or x0 == x2 or x1 == x2:
        return "Error: Los valores de x deben ser distintos entre sí."

    # Fórmula de Lagrange
    l0 = ((x_obj - x1) * (x_obj - x2)) / ((x0 - x1) * (x0 - x2))
    l1 = ((x_obj - x0) * (x_obj - x2)) / ((x1 - x0) * (x1 - x2))
    l2 = ((x_obj - x0) * (x_obj - x1)) / ((x2 - x0) * (x2 - x1))
    
    y = (y0 * l0) + (y1 * l1) + (y2 * l2)
    return f"Resultado: Para x={x_obj}, el valor de y es {y}"

def interpolacion_segmentada():
    print("\n--- Interpolación Lineal Segmentada ---")
    try:
        n = int(input("¿Cuántos puntos vas a ingresar? (mínimo 2): "))
        if n < 2:
            return "Error: Se necesitan al menos 2 puntos."
    except ValueError:
        return "Error: Por favor ingresa un número entero válido."

    puntos = []
    for i in range(n):
        x = float(input(f"Ingresa x{i}: "))
        y = float(input(f"Ingresa y{i}: "))
        puntos.append((x, y))
        
    # Es vital ordenar los puntos según x para que los segmentos tengan sentido
    puntos.sort(key=lambda p: p[0])
    
    x_obj = float(input("¿Qué valor de x quieres encontrar?: "))
    
    # Buscar el segmento correcto [x_i, x_{i+1}] donde se encuentra x_obj
    for i in range(n - 1):
        x0, y0 = puntos[i]
        x1, y1 = puntos[i+1]
        
        # Comprobar si x_obj está dentro del segmento actual
        # Si es mayor al último punto, usamos el último segmento (extrapolación por la derecha)
        # Si es menor al primer punto, usamos el primer segmento (extrapolación por la izquierda)
        if (x0 <= x_obj <= x1) or (i == 0 and x_obj < x0) or (i == n - 2 and x_obj > x1):
            if x1 == x0:
                return f"Error: Los puntos x{i} y x{i+1} tienen el mismo valor en x ({x0})."
                
            y = y0 + ((y1 - y0) / (x1 - x0)) * (x_obj - x0)
            return f"Resultado: Para x={x_obj}, usando el segmento [{x0}, {x1}], el valor de y es {y}"
            
    return "Error inesperado al calcular la interpolación."

def menu():
    while True:
        print("\n--- CALCULADORA DE INTERPOLACIÓN ---")
        print("1. Lineal (2 puntos)")
        print("2. Cuadrática (3 puntos)")
        print("3. Segmentada (n puntos)")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            print(interpolacion_lineal())
        elif opcion == '2':
            print(interpolacion_cuadratica())
        elif opcion == '3':
            print(interpolacion_segmentada())
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()