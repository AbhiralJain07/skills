//  package lecture3;

 import java.util.*;
 public class conditional_statements{
         public static void main(String[] args){

             Scanner sc = new Scanner(System.in);
             System.out.println("Enter your age :");
             int age = sc.nextInt();
             if (age>18) {
                 System.out.println("Adult");
             }
             else{
             System.out.println("Not Adult");
             }
        }
 }



 //2 -->>
// import java.util.*;
//
 class even {
     public static void main (String args[]){
         Scanner sc = new Scanner(System.in);

         int x = sc.nextInt();


         if (x%2 == 0){
             System.out.println("Even number");
         }

         else{
             System.out.println("Odd Number");
         }
     }
 }



 // -->> 3

// import java.util.*;

 class Comparison{

     public static void main(String[] args) {

         Scanner sc = new Scanner(System.in);

         int a = sc.nextInt();
         int b = sc.nextInt();

         if (a==b){
             System.out.println("A is equal to B");
         }
         else if(a>b){
                 System.out.println("A is grater than b");
         }
         else{
                 System.out.println("A is smaller than b");
         }

     }
 }
