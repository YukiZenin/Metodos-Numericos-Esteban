import sympy as sp

def diferenciacion_numerica():
    x_sym = sp.symbols('x')
    
    # 1. Ingreso de la función
    f_input = input("Ingresa la función f(x) (ej. exp(x), x**3): ")
    f = sp.lambdify(x_sym, f_input)
    
    # 2. Ingreso del punto y el paso
    x = float(input("Punto donde evaluar la derivada (x): "))
    h = float(input("Tamaño del paso (h) (ej. 0.01): "))

    # --- Cálculos ---
    
    # Diferencia Progresiva (Forward): [f(x + h) - f(x)] / h
    progresiva = (f(x + h) - f(x)) / h
    
    # Diferencia Regresiva (Backward): [f(x) - f(x - h)] / h
    regresiva = (f(x) - f(x - h)) / h
    
    # Diferencia Central (Centered): [f(x + h) - f(x - h)] / (2h)
    central = (f(x + h) - f(x - h)) / (2 * h)

    # --- Resultados ---
    print("\n" + "="*30)
    print(f"Resultados en x = {x} (h = {h})")
    print("-" * 30)
    print(f"Diferencia Progresiva: {progresiva:.6f}")
    print(f"Diferencia Regresiva:  {regresiva:.6f}")
    print(f"Diferencia Central:    {central:.6f}")
    print("="*30)

diferenciacion_numerica()