import numpy as np

def taylor_orden_2(f, df, x0, y0, h, x_end):
    """Resuelve la EDO usando el método de Taylor de orden 2."""
    # Calcular el número de pasos
    n_steps = int(np.round((x_end - x0) / h))
    
    # Crear arreglos para los resultados
    x_vals = np.linspace(x0, x_end, n_steps + 1)
    y_vals = np.zeros(n_steps + 1)
    
    # Condición inicial
    y_vals[0] = y0
    
    # Bucle iterativo
    for i in range(n_steps):
        xi = x_vals[i]
        yi = y_vals[i]
        
        y_prima = f(xi, yi)
        y_biprima = df(xi, yi)
        
        # Fórmula de Taylor de orden 2
        y_vals[i+1] = yi + h * y_prima + (h**2 / 2) * y_biprima
        
    return x_vals, y_vals

# =====================================================================
# CONFIGURACIÓN DE LAS FUNCIONES (Modifícalas según tu ejercicio)
# =====================================================================
# Ejemplo por defecto: y' = x - y  =>  y'' = 1 - x + y

def f(x, y):
    return x - y  # <- Aquí va tu primera derivada (y')

def df(x, y):
    return 1 - x + y  # <- Aquí va tu segunda derivada (y'')


# =====================================================================
# BLOQUE DE ENTRADA DE DATOS (INTERACTIVO)
# =====================================================================
print("=" * 50)
print("       MÉTODO DE TAYLOR DE ORDEN 2 (INTERACTIVO)       ")
print("=" * 50)
print("Nota: Recuerda cambiar las funciones f(x,y) y df(x,y) dentro")
print("del código si tu problema es diferente al ejemplo (y' = x - y).\n")

try:
    # El usuario ingresa los valores por consola
    x_inicial = float(input("1. Introduce el valor inicial de x (x0): "))
    y_inicial = float(input("2. Introduce el valor inicial de y (y0): "))
    paso_h = float(input("3. Introduce el tamaño de paso (h): "))
    x_final = float(input("4. Introduce el valor final de x a evaluar (x_end): "))

    # Validaciones rápidas para evitar que el programa se rompa o cicle
    if paso_h <= 0:
        print("\n[!] ¡Ojo! El tamaño de paso (h) debe ser un número positivo.")
    elif x_final <= x_inicial:
        print("\n[!] Error: El valor final de x debe ser mayor que el inicial.")
    else:
        # Calcular el método con los datos del usuario
        x_res, y_res = taylor_orden_2(f, df, x_inicial, y_inicial, paso_h, x_final)

        # Mostrar los resultados formateados en una tabla
        print("\n" + "=" * 50)
        print("                   RESULTADOS OBTENIDOS                ")
        print("=" * 50)
        print(f"{'Iteración':<10} | {'x':<10} | {'y (Aproximación)':<20}")
        print("-" * 50)
        
        for i, (x, y) in enumerate(zip(x_res, y_res)):
            print(f"{i:<10} | {x:<10.4f} | {y:<20.6f}")
        print("=" * 50)

except ValueError:
    print("\n[!] Error: Por favor, introduce solo números válidos (usa el punto '.' para los decimales).")