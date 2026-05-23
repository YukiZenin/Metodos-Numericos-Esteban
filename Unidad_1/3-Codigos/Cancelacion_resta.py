def main():
    x = 1234567890.1234561
    y = 1234567890.1234560
    resultado = x - y
    
    print(f"Resultado esperado: {0.0000001}")
    print(f"Resultado real: {resultado} Erp")

if __name__ == "__main__":
    main()