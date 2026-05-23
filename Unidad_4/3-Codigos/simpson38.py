import sympy as sp

def simpson_38_simple():
    x = sp.symbols('x')
    
    f_input = input("Ingresa la función f(x): ")
    f = sp.lambdify(x, f_input)
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))

    # Tamaño del paso
    h = (b - a) / 3
    x1 = a + h
    x2 = a + 2*h

    # Fórmula: (3h / 8) * [f(a) + 3f(x1) + 3f(x2) + f(b)]
    resultado = (3 * h / 8) * (f(a) + 3*f(x1) + 3*f(x2) + f(b))
    
    print(f"\nResultado (Simpson 3/8): {resultado}")

simpson_38_simple()