package Lecture10;

// arrays 

// defining array - method 1

// store the marks of students in the array

// import java.util.*;
// public class class_1 {

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int n = sc.nextInt();

//         int marks [] = new int[3];
//         marks[0] = 92;
//         marks[1] = 94;
//         marks[2] = 90;

//         System.out.println(marks[0]);
//         System.out.println(marks[1]);   //ye wale method mai hme ek-ek krke number print krwana hota h
//         System.out.println(marks[2]);
//     }
// }


//using FOR loop - loop lgane se saare marks ek baar mai print ho jayenge

 import java.util.*;
 public class class_1 {

     public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         int n = sc.nextInt();

         int[] marks = new int[n];
         marks[0] = 92;
         marks[1] = 94;
         marks[2] = 90;

         for (int i =0 ; i<n; i++){
             System.out.println(marks[i]);
         }

     }
 }