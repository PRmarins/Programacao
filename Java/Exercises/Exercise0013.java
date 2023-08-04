import java.util.Scanner;

public class Exercise0013 {
    
    public static void main(String [] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite dois números para somar: ");
        
        System.out.println("Primeiro número: ");
        int numero1 = teclado.nextInt();
        
        System.out.println("Segundo número: ");
        int numero2 = teclado.nextInt();

        int c = soma(numero1,numero2);


        System.out.println(c);
       
        teclado.close();
    }

    public static int soma (int a , int b) {
        return a + b;
    }
}
