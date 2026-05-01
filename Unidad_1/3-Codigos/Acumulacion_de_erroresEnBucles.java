package acumulacion_de_errores.en.bucles;
public class Acumulacion_de_erroresEnBucles {
    public static void main(String[] args) {
        int iteraciones = 3000000;
        double incremento = 0.3;
        double sumaDouble = 0.0;
        for (int i = 0; i < iteraciones; i++) {
            sumaDouble += incremento;
        }
        double esperado = iteraciones * incremento;
        System.out.println("El resultado esperado deberia ser exactamente 100,000.0");
        System.out.println("Acumulacion en Bucle (1,000,000 de iteraciones)");
        System.out.println("Resultado esperado: " + esperado);
        System.out.println("Resultado double:   " + sumaDouble);
        System.out.println("Diferencia (Error): " + (sumaDouble-esperado));
        java.math.BigDecimal sumaBD = java.math.BigDecimal.ZERO;
        java.math.BigDecimal incrementoBD = new java.math.BigDecimal("0.1");
        for (int i = 0; i < iteraciones; i++) {
            sumaBD = sumaBD.add(incrementoBD);
        }
        System.out.println("\nSolucion con BigDecimal");
        System.out.println("Resultado real:   " + sumaBD.toPlainString());     
        if (sumaDouble != esperado) {
            System.out.println("\nNota: El error de double es notable tras un millon de sumas. Erp");
        }

    }
    
}
