import sympy as sp

def simpson_13_simple():
    x = sp.symbols('x')
    
    f_input = input("Ingresa la función f(x): ")
    f = sp.lambdify(x, f_input)
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))

    # Punto medio
    h = (b - a) / 2
    m = a + h

    # Fórmula: (h / 3) * [f(a) + 4f(m) + f(b)]
    resultado = (h / 3) * (f(a) + 4*f(m) + f(b))
    
    print(f"\nResultado (Simpson 1/3): {resultado}")

simpson_13_simple()