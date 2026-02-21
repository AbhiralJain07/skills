// Inverted HAlf Pyramid (rotated by 180)
package lecture5;

public class class_5 {
    public static void main(String[] args) {
        int n =4 ;
        

        //outer loop -->> for rows
        for(int i =1; i<=n ; i++ ){

            // inner loop -->> for spaces
            for(int j =1 ; j<=n-i ; j++){
                System.out.print(" ");
            }

            // inner loop -->> for stars
                for (int j =1 ; j<=i ; j++){
                    System.out.print("*");
                }
                
            
            System.out.println();
        }
    }
}
