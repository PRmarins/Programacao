public class Exercise0016 {
    
    public static void main (String [] args) {

        
        //########## VERIFICAR SE UMA STRING É IGUAL A OUTRA ##########//
         
        String s1 = "ola";
        String s2 = "ola";
        String s3 = "bosta";

        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(s3));

        // ########## PASSAR TUDO PRA MAIUSCULO OU MINUSCULO ##########

        String s4 = "tesTaNdo";
        
        System.out.println(s4.toUpperCase()+", "+s4.toLowerCase());

        // ########## VERIFICAR SE POSSUE CERTO ELEMENTO DENTRO ##########//

        String s5 = "Fui a praia porém nao gostei";

        System.out.println(s5.contains("praia"));
        System.out.println(s5.contains("shopping"));

        //########## VERIFICAR SE INICIA OU TERMINA COM UMA CADEIA ESPECÍFICA DE CARACTERES ##########//

        String s6 = "Como nao tinha fome não comi.";

        System.out.println(s6.startsWith("não"));
        System.out.println(s6.startsWith("Como"));

        System.out.println(s6.endsWith("comi."));
        System.out.println(s6.endsWith("carne"));

        //########## SUBSTITUIR CARACTERES ##########//

        String s7 = "Foi um grande jogo, mas perdemos";

        System.out.println(s7.replace("perdemos", "ganhamos"));

        // ########## SEPARAR TERMOS EM ARRAY ##########//

        String s8 = "Ola a todos que estao aqui.";

        String s8Split [] = s8.split(" ");

        System.out.println(s8Split[2]+" "+s8Split[0]);

        for (int i = 0; i < s8Split.length; i++) { 

            System.out.print(s8Split[i] +" ");
        }

        

    }
}
