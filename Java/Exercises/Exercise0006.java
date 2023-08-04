import java.util.Scanner;

public class Exercise0006 {
    
    public static void main (String [] args) {

        Scanner teclado = new Scanner (System.in);

        System.out.println("Qual dia da semana em ingles deseja consultar? (Digite números entre 1 e 7.)");
        int dia = teclado.nextInt();

        switch (dia) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Dia não encontrado.");
        }teclado.close();

    }
    
}
