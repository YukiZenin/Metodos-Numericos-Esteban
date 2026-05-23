def main():
    max_int = 2147483647 # Equivalente a Integer.MAX_VALUE en Java
    resultado = max_int + 10000
    
    print(f"Maximo int: {max_int}")
    print(f"Maximo + 10000: {resultado}") # En Python, esto suma perfectamente sin desbordarse.
    
    # Simulando el desbordamiento que capturaría Math.addExact
    try:
        suma_exacta = max_int + 10
        if suma_exacta > 2147483647:
            raise OverflowError("Error detectado: Desbordamiento Erp")
    except OverflowError as e:
        print(e)

if __name__ == "__main__":
    main()