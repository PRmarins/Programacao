package Java.Beecrowd.Exercises;

import java.util.Scanner;

public class Exercise1001 {
    
    public static void main (String [] args) {

        System.out.println("Escolha dois numeros para somar: ");

        Scanner teclado = new Scanner(System.in);
        int A = teclado.nextInt();
        int B = teclado.nextInt();

        soma(A,B);
    }
    
    public static Integer soma (int A, int B){
        int X = A + B;
        
        System.out.println("X = " + X);

        return X;


    }
}