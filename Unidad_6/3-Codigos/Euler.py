import numpy as np

def euler_metodo(f, x0, y0, h, x_end):
    """Resuelve la EDO usando el método de Euler hacia adelante."""
    # Calcular el número de pasos
    n_steps = int(np.round((x_end - x0) / h))
    
    # Crear arreglos para los resultados
    x_vals = np.linspace(x0, x_end, n_steps + 1)
    y_vals = np.zeros(n_steps + 1)
    
    # Condición inicial
    y_vals[0] = y0
    
    # Bucle iterativo de Euler
    for i in range(n_steps):
        xi = x_vals[i]
        yi = y_vals[i]
        
        # Fórmula de Euler: y_siguiente = y_actual + h * f(x, y)
        y_vals[i+1] = yi + h * f(xi, yi)
        
    return x_vals, y_vals

# =====================================================================
# CONFIGURACIÓN DE LA FUNCIÓN (Modifícala según tu ejercicio)
# =====================================================================
# Ejemplo por defecto: y' = x - y

def f(x, y):
    return x - y  # <- ¡Aquí solo va tu primera derivada! Mucho más simple.


# =====================================================================
# BLOQUE DE ENTRADA DE DATOS (INTERACTIVO)
# =====================================================================
print("=" * 50)
print("           MÉTODO DE EULER (INTERACTIVO)               ")
print("=" * 50)
print("Nota: Recuerda cambiar la función f(x,y) dentro del código")
print("si tu problema es diferente al ejemplo (y' = x - y).\n")

try:
    # El usuario ingresa los valores por consola
    x_inicial = float(input("1. Introduce el valor inicial de x (x0): "))
    y_inicial = float(input("2. Introduce el valor inicial de y (y0): "))
    paso_h = float(input("3. Introduce el tamaño de paso (h): "))
    x_final = float(input("4. Introduce el valor final de x a evaluar (x_end): "))

    # Validaciones
    if paso_h <= 0:
        print("\n[!] ¡Ojo! El tamaño de paso (h) debe ser un número positivo.")
    elif x_final <= x_inicial:
        print("\n[!] Error: El valor final de x debe ser mayor que el inicial.")
    else:
        # Calcular el método
        x_res, y_res = euler_metodo(f, x_inicial, y_inicial, paso_h, x_final)

        # Mostrar los resultados
        print("\n" + "=" * 50)
        print("                   RESULTADOS OBTENIDOS                ")
        print("=" * 50)
        print(f"{'Iteración':<10} | {'x':<10} | {'y (Aproximación)':<20}")
        print("-" * 50)
        
        for i, (x, y) in enumerate(zip(x_res, y_res)):
            print(f"{i:<10} | {x:<10.4f} | {y:<20.6f}")
        print("=" * 50)

except ValueError:
    print("\n[!] Error: Por favor, introduce solo números válidos.")