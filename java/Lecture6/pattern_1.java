//Butterfly Pattern

package Lecture6;

// import lecture4.forloop;

public class pattern_1 {
    public static void main(String[] args) {
        int n = 5;

        //outer loop
        for(int i=1; i<=n ; i++){

            //First half -> Upper half
            for(int j =1 ; j <=i; j++){
                System.out.print("*");
            }

            //spaces
            int spaces = 2*(n-i);
            for(int j =1 ; j<= spaces; j++){
                System.out.print(" ");
            }

            //2nd part:
            for(int j =1; j<=i; j++){
                System.out.print("*");
            }
            System.out.println();
        }


        //Second Half (lower loop)
        for(int i=n; i>=1 ; i--){
            for(int j =1 ; j <=i; j++){
                System.out.print("*");
            }

            //spaces
            int spaces = 2*(n-i);
            for(int j =1 ; j<= spaces; j++){
                System.out.print(" ");
            }

            //2nd part:
            for(int j =1; j<=i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
