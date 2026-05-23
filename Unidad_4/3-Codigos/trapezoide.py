import sympy as sp

def trapezoide_simple():
    x = sp.symbols('x')
    
    # Entradas del usuario
    f_input = input("Ingresa la función f(x) (ej. x**2 + 1): ")
    f = sp.lambdify(x, f_input)
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))

    # Fórmula: (b - a) * [f(a) + f(b)] / 2
    resultado = (b - a) * (f(a) + f(b)) / 2
    
    print(f"\nResultado (Trapezoide Simple): {resultado}")

trapezoide_simple()