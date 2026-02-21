package Lecture10;

// store the marks of students in the array
// by defining the array - method 2

 import java.util.Scanner;

 public class class_2 {
     public static void main(String[] args){

         Scanner sc = new Scanner(System.in);
//         int number = sc.nextInt();
         int size = sc.nextInt();

         int[] number = new int[size];
         for (int i = 0; i<size ; i++){
             number[i] = sc.nextInt();
         }
         for (int i = 0; i<size; i++){
             System.out.println(number[i]);
         }
     }
 }
