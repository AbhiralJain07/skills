# x = 0
# y = 0
# if x>0:
#     y = y=1
# else:
#     if x<0:
#         y = y+2
#     else:
#         y = y+5
#         print("Y = ", y)

# x = 10
# y = 50
# if (x**2 > 100 and y < 100):
#     print(x,y)

# i = int (input("Enter Number : "))
# j = int (input("Enter Number : "))
# k = int (input("Enter Number : "))

# if j>k : 
#     if i>k:
#         num = i
#     else:
#         num = j
# else :
#     if i > k :
#         num = i
#     else:
#         num = k 

# print("greatest number : ", num)

# i = 5
# k = 15
# print(k%i < k/i)

### Section B

# i =1 
# while i<=100:
#     print(i)
#     i += 1

## WAP to find number of digits of an integar

# num = int(input("Enter Number : "))
# x = num
# i = 0
# while num >0:
#     num = num //10
#     i +=1
#     print("The number of digits in the entered number : ", x , "is : ", i)


## WAP to reverse a number

# num = int (input("Enter Number : "))
# x = num
# rev = 0

# while num>0:
#     rem = num %10
#     num = num //10
#     rev = rev*10 + rem

# print("Reverse of number is : ", rev)

##SOL2
# a = int(input("Enter Number : "))
# rev = (a% 10)*10 + (a//10)
# print("Reversed Number : ", rev)


# n = int(input("Enter Number : "))
# i = 0
# while i<= n:
#     print(5**i) 
#     i += 1

# for i in range (1,6):
#     print(i)

## Doubt.  
# print("The Capital Letters A to Z are : ")
# for i in range (65,91):
#     print(chr(i), end = "")

# print("Numbers from 1 to 10 in reverse order : ")
# for i in range (10 , 0 ,-1):
#     print(i)

# for i in range (1,7):
#     for j in range(1,i):
#         print("*" , end="")
#     print("*")

# full pyramid
# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):

#     # print spaces
#     for _ in range(rows - i):
#         print(" ", end="")

#     # print stars
#     for _ in range(2 * i - 1):
#         print("*", end="")

#     print()


# for i in range (5 , 0 ,-1):
#     for j in range (1 , i+1):
#         print(j , end = "")
#     print()


# a = int (input ("Enter number : "))
# b = int (input ("Enter number : "))
# c = int (input ("Enter number : "))

# largest = a

# if b >largest:
#     largest = b

# if c > largest :
#     largest = c

# print(largest)

# num = int (input ("Enter Number : "))
# if num %2 :
#     print("Odd")
# else :
#     print("Even")

# for i in range (1 , 20):
#     if i%3==0 or i%5 == 0:
#         continue
#     print(i)

# ch = chr(input("")) 
# if len(ch) != 1:
#     print("Please enter a single character")
# else:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             print("vowel")
#         else:
#             print("consonant")
#     elif ch.isdigit():
#         print("digit")
#     else:
#         print("special character")

# n = (int(input()))
# if n == 0:
#     print("even digits: 1")
#     print("odd digits: 0")
# else:
#     even = odd = 0
#     while n > 0:
#         d = n % 10
#         if d % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#         n //= 10
#     print("even digits:", even)
#     print("odd digits:", odd)

# a = int (input (" "))
# b = int ( input(" "))
# lcm= max(a,b)
# while True:
#     if lcm % a==0 and lcm % b ==0 :
#         print(f"lcm of {a} and {b} is {lcm}")
#         break
#     lcm +=1


# for i in range (1,101):
#     if (i%3 == 0 and i%5 == 0):
#         print("FizzBuzz")
#     elif (i%3 ==0):
#         print("Fizz")
#     elif (i%5 == 0):
#         print("Buzz")
#     else:
#         print(i)

# n = 5
# for i in range (n):
#     if i == 0 or i == n-1:
#         print("*"*n)
#     else:
#         print("*" + " "*(n-2) + "*")

# rows = 4
# coloumns = 5

# for i in range (rows):
#     for j in range (coloumns):
#         if (i+j)%2 == 0:
#             print("1" , end = "")
#         else:
#             print("0" , end ="")
#     print()

# L1=[10,20,30,40,50,60]
# print(L1[0:5:2])
# print(L1[:3])
# print(L1[::-1])
# print(L1[-1:0:-1])

# colour_list = ["Red", "Green", "White" ,"Black"]
# print("The first colour of the list is ",colour_list[0])
# print("The last colour of the list is ", colour_list[-1])

# year = int(input("Enter a year: "))
# is_leap = (year % 4 == 0) * (year % 100 != 0) + (year % 400 == 0)
# if is_leap:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# def list_of_even_numbers (start , end):
#     output_list = []
#     for i in range (start , end) :
#         if i%2 ==0:
#             output_list.append(i)
#     print(output_list)
# a,b=input("Enter the values for a and b: ").split()
# list_of_even_numbers(int(a), int(b))



# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range (1,7):
#     for j in range(i,6):
#         print(" ", end= " ")
#     for j in range(1,i+1):
#         print(" * ",end=" ")
#     print()

# for i in range (5,0,-1):
#     for j in range(1,i+1):
#         print(j , end="")
#     print()

# def fib(n):
#     if n==0 or n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)
# n = int(input (""))
# print("fib num :", fib(n))

# for i in range (10 , 0 ,-1):
#     print(i , end=" ")
