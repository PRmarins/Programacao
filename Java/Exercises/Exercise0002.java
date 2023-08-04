public class Exercise0002 {
    public static void main (String [] args) {
        System.out.println("EXERCICIO 2");

        int numeroInicio = 5;
        int numeroFin = 14;
        int x = numeroInicio -1;

        while (x <= numeroFin) {
            x += 1;
            if (x % 2 == 0) {
                System.out.println(x);           
            } 
            
        }

    }
    
}
