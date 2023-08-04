import java.util.Scanner;

public class Exercise0012 {

    public static void main ( String [] args) {

        System.out.println("Diga dois números` e vamos ver se a soma é par ou impar: ");
        
        Scanner teclado = new Scanner(System.in);
        int num = teclado.nextInt();
      
        if (espar(num)){

            System.out.println("El número es par.");
        }else{

            System.out.println("El número es impar.");
        }teclado.close();

    }

    public static boolean espar(int num){

        int resto = num % 2;
         if (resto == 0){
            return true;
        }else {
            return false;
        }
        

    }
    
}
