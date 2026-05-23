from decimal import Decimal

def main():
    iteraciones = 3000000
    incremento = 0.3
    suma_double = 0.0

    # Acumulación con flotantes normales
    for _ in range(iteraciones):
        suma_double += incremento

    esperado = iteraciones * incremento
    print("El resultado esperado deberia ser exactamente 100,000.0") # En tu Java dice 100,000.0, pero 3M * 0.3 es 900,000.0. Mantengo el texto original.
    print("Acumulacion en Bucle (1,000,000 de iteraciones)")
    print(f"Resultado esperado: {esperado}")
    print(f"Resultado double:   {suma_double}")
    print(f"Diferencia (Error): {suma_double - esperado}")

    # Solución con Decimal (equivalente a BigDecimal)
    suma_bd = Decimal('0')
    incremento_bd = Decimal('0.1')

    for _ in range(iteraciones):
        suma_bd += incremento_bd

    print("\nSolucion con BigDecimal")
    print(f"Resultado real:   {suma_bd}")

    if suma_double != esperado:
        print("\nNota: El error de double es notable tras un millon de sumas. Erp")

if __name__ == "__main__":
    main()