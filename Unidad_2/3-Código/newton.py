import time

def newton_raphson(f, df, x0, tol, max_iter=50):
    for i in range(max_iter):
        derivada = df(x0)
        if derivada == 0:
            return "Error: Derivada cero"
            
        x1 = x0 - f(x0) / derivada
        
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        
    return "Diverge o no converge en el límite de iteraciones"

print("\n--- MÉTODO DE NEWTON-RAPHSON ---")

# Problema 1
f1 = lambda x: x**3 - x - 1
df1 = lambda x: 3*x**2 - 1
inicio = time.perf_counter()
raiz1 = newton_raphson(f1, df1, 2, 0.05)
fin = time.perf_counter()
print(f"Problema 1 -> Raíz: {raiz1:.6f} | Tiempo: {fin-inicio:.8f} seg")

# Problema 2 (El que diverge)
f2 = lambda x: x**2 + 6*x + 10
df2 = lambda x: 2*x + 6
inicio = time.perf_counter()
raiz2 = newton_raphson(f2, df2, 1, 0.05)
fin = time.perf_counter()
print(f"Problema 2 -> Raíz: {raiz2} | Tiempo: {fin-inicio:.8f} seg")