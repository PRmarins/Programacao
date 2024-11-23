import java.util.Scanner;
import java.util.Locale;

public class arquivo1 {
    public static void main (String [] args){
        Scanner teclado = new Scanner(System.in);
        teclado.useLocale(Locale.US);

        /*
        System.out.println("Ola, pode me dizer seu nome?");
        String nome = teclado.nextLine();
        
        System.out.println("Olá " + nome + " como vai você?");

        System.out.println(nome+" pode me dizer onde você mora?");
        String cidade = teclado.nextLine();

        System.out.println("Que legal, ouvi dizer que "+ cidade+" é um lugar muito bonito!");
        */
        
        float primeiroNumero = teclado.nextFloat();
        float segundoNumero = teclado.nextFloat();

        float conta = primeiroNumero * segundoNumero;

        System.out.println(conta);


    }
    
}
