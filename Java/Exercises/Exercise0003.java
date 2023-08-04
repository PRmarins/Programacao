import java.util.Scanner;

public class Exercise0003 {
    public static void main ( String [] args) {
        System.out.println("Ola mundo!");
        System.out.println("Numero do 4 ao 15.");
        System.out.println("Escolha se mostra os números impares ou pares:");

        int inicionumero = 4;
        int finalnumero = 15;
        int x = inicionumero - 1;
        
        Scanner teclado = new Scanner(System.in);

        System.out.println("Para PAR [ 0 ],  para IMPAR [ 1 ]");
        int parimpar = teclado.nextInt();
        
        if (parimpar == 0) {
            System.out.println("OS números pares são:");
            while (x < finalnumero) {
                x +=1;
                if (x % 2 == 0){
                    System.out.println(x);
                }
            }
        }
        
        if (parimpar == 1) {
            System.out.println("Os números impares são:");
            while (x < finalnumero){
                x += 1;
                if (x % 2 != 0) {
                    System.out.println(x);
                }

            }
        }teclado.close();       

    }
}