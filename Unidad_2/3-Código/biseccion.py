import time

def biseccion(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return None
        
    xr = a
    while (b - a) / 2.0 > tol:
        xr = (a + b) / 2.0
        if f(xr) == 0:
            break
        elif f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
    return (a + b) / 2.0

print("\n--- MÉTODO DE BISECCIÓN ---")

# Función 1
f1 = lambda x: 2*x**2 - 3
inicio = time.perf_counter()
raiz1 = biseccion(f1, -1, 2, 0.05)
fin = time.perf_counter()
print(f"Función 1 (2x^2 - 3) -> Raíz: {raiz1:.6f} | Tiempo: {fin-inicio:.8f} seg")

# Función 2
f2 = lambda x: x**3 - 4*x - 9
inicio = time.perf_counter()
raiz2 = biseccion(f2, 2, 3, 0.01)
fin = time.perf_counter()
print(f"Función 2 (x^3 - 4x - 9) -> Raíz: {raiz2:.6f} | Tiempo: {fin-inicio:.8f} seg")