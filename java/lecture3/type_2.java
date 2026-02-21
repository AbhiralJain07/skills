//  package lecture3;


 import java.util.*;
 public class type_2 {
      public static void main(String[] args) {
        
         Scanner sc = new Scanner(System.in);
         System.out.print("Enter Button :");
         int button = sc.nextInt();

         switch (button) {
             case 1:
                 System.out.println("Hello");
                 break;

             case 2:
                 System.out.println("Namaste");
                 break;

             case 3:
                 System.out.println("Bonjour");
                 break;
        
             default:
                 break;
         }
     }
 }

