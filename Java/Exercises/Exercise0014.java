import java.util.Scanner;

public class Exercise0014 {
    
    public static void main (String [] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.println("Que operação gostaria de fazer?");
        System.out.println("[+] para somar      [-] para subtrair      [*] para multiplicar      [/] para dividir.");
        
        String resposta = teclado.nextLine();

        
            //########## SOMAR ##########//
         

        if (resposta.equals("+")) {
            
            System.out.println("Quais números você quer somar?");
            int a = teclado.nextInt();
            int b = teclado.nextInt();

            int c = soma(a, b);

            System.out.println("A soma entre "+a+ " e "+b+" é igual a "+c+".");

        }
        
            //########## SUBTRAIR ##########//

        else if (resposta.equals("-")) {
        
            System.out.println("Quais números você quer subtrair?");
            int a = teclado.nextInt();
            int b = teclado.nextInt();

            int c = subtrair(a, b);

            System.out.println("O número "+a+" menos o número "+b+" é igual a "+c+".");

        
        }
        
            //########## MULTIPLICAR ##########//

        else if (resposta.equals("*")) {

            System.out.println("Que números você quer multiplicar?");
            int a = teclado.nextInt();
            int b = teclado.nextInt();

            int c = multiplicar(a, b);

            System.out.println("O número "+a+" multiplicado por "+b+" é igual a "+c+".");
        

        }
        
            //########## DIVIDIR ##########//
        
        else if (resposta.equals("/")) {

            System.out.println("Quais números você quer dividir?");
            Double a = teclado.nextDouble();
            Double b = teclado.nextDouble();

            double c = dividir(a, b);
            String result = String.format("%.2f", c);

            System.out.println("O número "+a.intValue()+" dividido por "+b.intValue()+" da igual a "+result+".");

        }
        
            //########## ERRO ##########//
        
        else {
           
            System.out.println("Resposta inválida.");

        }teclado.close();
    }

    public static int soma (int a, int b) {
        return a + b;
    }

    public static int subtrair (int a, int b) {
        return a - b;
    }

    public static int multiplicar (int a, int b)  {
        return a * b;
    }

    public static double dividir (Double a, Double b) {
        return a / b;
    }


}