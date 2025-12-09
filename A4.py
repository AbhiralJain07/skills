# a = abs(-43)
# print(a)

# import math
# x = 4
# print(math.sqrt(x))

# import random
# a =random.uniform(9,99)
# print(a)

# import calendar
# cal = calendar.month(2006,7)
# print("Here is the calendar:" , cal)

# from time import process_time
# start = process_time()
# name = input('Enter your name: ')
# time_passed = process_time()-start
# print(name,',you took',time_passed,'seconds to write your name.')

##recursive 

# def fact(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return (n *fact(n-1))
# n = int (input(" "))
# print("The Factorial of", n , "is:",fact(n))

# def power(x,n):
#     if (n==1):
#         return x
#     else :
#         return x *power(x , n-1)
# x = int (input("enter base :"))
# n = int (input("Enter exp :"))
# print(x,"raised to", n ,"is",power(x,n) )

# def sum_of_digit(n):
#     if n == 1:
#         return 1
#     return(n%10 + n//10)
# n = int (input("Enter Number :"))
# print("the sum of the digits is :",sum_of_digit(n))

# def gcd(a,b):
#     if b==0:
#         return a
#     elif b==1 :
#         return 1
#     else:
#         return(gcd(b,a%b))
# print("Enter Two number ")
# a = int (input(" "))
# b = int (input(" "))
# print("the GCD is " , gcd(a,b))

# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n = int(input(" "))
# print("The fib series is" , fib(n))

# def rec_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + rec_sum(n-1)
# n = int(input(" "))
# print("the recursive sum is : ", rec_sum(n))