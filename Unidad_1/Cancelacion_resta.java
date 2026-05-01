package cancelacion_resta;
public class Cancelacion_resta {
    public static void main(String[] args) {
        double x = 1234567890.1234561;
        double y = 1234567890.1234560;
        double resultado = x - y;
        System.out.println("Resultado esperado: "+0.0000001);
        System.out.println("Resultado real: " + resultado+" Erp"); 
    }
}

