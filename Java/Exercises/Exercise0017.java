public class Exercise0017 {
    
    public static void main (String [] args){
        
        meuMetodo();

        int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
    for (int i = 0; i < myNumbers.length; ++i) {
      for(int j = 0; j < myNumbers[i].length; ++j) {
        System.out.println(myNumbers[i][j]);
      }
    
    }   
    
    }
    static void meuMetodo (){
        System.out.println("Comecando a executar.");
    }

}