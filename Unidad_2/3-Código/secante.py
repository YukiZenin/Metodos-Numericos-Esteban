import math
import time

def secante(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            return None # Evita división por cero
            
        # Fórmula de la secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if abs(x2 - x1) < tol:
            return x2
            
        x0, x1 = x1, x2
    return x2

print("--- MÉTODO DE LA SECANTE ---")

# Caso 1
f1 = lambda x: x**2 - 4
inicio = time.perf_counter()
raiz1 = secante(f1, 1, 3)
fin = time.perf_counter()
print(f"Caso 1 (x^2 - 4) -> Raíz: {raiz1:.6f} | Tiempo: {fin-inicio:.8f} seg")

# Caso 4 (Usando valores iniciales comunes 0 y 1)
f2 = lambda x: math.cos(x) - x
inicio = time.perf_counter()
raiz2 = secante(f2, 0, 1)
fin = time.perf_counter()
print(f"Caso 4 (cos(x) - x) -> Raíz: {raiz2:.6f} | Tiempo: {fin-inicio:.8f} seg")