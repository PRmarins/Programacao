import java.util.Scanner;


public class Exercise0007 {
    
    public static void main (String [] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite um número para que comece a contar.");
        int finalNumber = teclado.nextInt();
        int i = 0;
        do {
            System.out.println(i);
            i++;
        }
        while (i < finalNumber + 1);
        teclado.close();

    }
}
