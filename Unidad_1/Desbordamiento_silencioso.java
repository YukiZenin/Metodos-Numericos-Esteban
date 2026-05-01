package desbordamiento_silencioso;
public class Desbordamiento_silencioso {
    public static void main(String[] args) {
        int max = Integer.MAX_VALUE; // 2,147,483,647
        int resultado = max + 10000;
        System.out.println("Maximo int: " + max);
        System.out.println("Maximo + 10: " + resultado);
        try {
            Math.addExact(max, 10);
        } catch (ArithmeticException e) {
            System.out.println("Error detectado: Desbordamiento Erp");
        }

    }
}
