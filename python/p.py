# ##practice

# i =1 
# while(i<=100):
#     print("Hello")
#     i += 1


# n = int (input("Enter number: "))
# fact = 1
# i = 1
# while i<= n:
#     fact*=i
#     i +=1
# print("factorial = ",fact)

# num= 2e3
# print(type(num))
# print(num)


# print(int(2.999))

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# print("hello")
# print(format("hello", ">20s"))

# P = float(input("Enter principal amount: "))
# r = float(input("Enter annual interest rate (%): "))
# t = float(input("Enter time in years: "))

# FV = P * (1 + r/100)**t
# print("Future Value =", round(FV, 2))


# num = int(input("Enter a two-digit number: "))
# rev = (num % 10) * 10 + (num // 10)
# print("Reversed number:", rev)

# x = 10
# def func():
#     x = 5
#     print(x)   # local
# func()
# print(x)       # global


# a = float(input())
# b = float(input())
# c = float(input())
# largest = a
# if b > largest:
#     largest = b
# if c > largest:
#     largest = c
# print(largest)

# a = int(input("ENTER NUMBER : "))
# if (a%2 == 0):
#     print("EVEN")
# else:
#     print("ODD")

# for i in range(1,21):
#     if (i%3 == 0 or i%5 == 0):
#         continue
#     print(i)

 
# print("hello")
# print(format("hello", ">20s"))

# feet = float(input("Enter distance in feet: "))
# inches = feet * 12
# yards = feet / 3
# miles = feet / 5280
# print(f"Inches: {inches}, Yards: {yards}, Miles: {miles}")


# sec = int(input("Enter time in seconds: "))
# hours = sec // 3600
# sec %= 3600
# minutes = sec // 60
# seconds = sec % 60
# print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


# amount = int(input("Enter amount: "))
# notes = [500, 200, 100, 50, 20, 10]
# for note in notes:
#     count = amount // note
#     amount %= note
#     if count:
#         print(f"{note} x {count}")


# num = float(input("Enter Number : "))
# integar = int(num)
# fraction = int((num - integar) *10)
# print("Integar : ", integar)
# print("Fraction : ", fraction)

# num = float(12.34)
# print(int(num))

# num = int(input("Enter Number : "))
# if num & 1 == 0:
#     print("Even")

# else:
#     print("Odd")

# print("Hello", end=' ')
# print("World")

# a = int(input())
# b = int(input())
# print("Sum:", a + b)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# print(type(5/2))
# print(type(5//2))

# print(3 < 5 < 7)
# print(3 < 5 > 7)

# print(int(False) + float(True))

# print(bool(0), bool(' '), bool([]), bool(None))

# str = "VIT Bhopal"
# print(str[::-1])

# print("2" * 3 + "3")

# str = "VIT"
# print(str * (len(str) - 1))

# str = "VIT"
# str += "Bhopal"
# print(str*2)

# print("VIT", "Bhopal", "University", sep='@', end='!')

# A,B = ("JAI SHREE RAM\n" ,10) 
# Txt="@"
# print((A+Txt)*B)

# print("abc" < "abcd")
# print("abc" < "abd")

# str1 = "a"
# str2 = "A"
# print(str1 > str2)

# print("123" > "99")

# print('Py' in 'Python')
# print('py' not in 'Python')

# if True: print("Hi")

# for i in range(5):
#     print(i)
#     i = i + 1
# else:
#     print("DONE")

# for i in range (5):
#     if i ==3:
#         break
#     print(i)
# else:
#     print("Done")

# x = 0
# while x<3 :
#     x += 1
#     if x == 2:
#         continue
#     print(x)

# a = 10
# b = 4
# print(a & b, a | b, a ^ b)

# str = "level"
# print(str == str[::-1])

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# print(18/4)
# print(18//4)
# print(-18//4)
# print(6%2)
# print(2%6)
# print(2**6)

# # print(2 ** 3 ** 2)
# print(2 * 3 ** 3 * 4)

# print(format(10.32245, ".2f"))
# print(format(10.345, ".3f"))
# print(format(10,".2f"))


# while True :
#     password = input("Enter password :")
#     if password== "python":
#         print("Correct")
#     else:
#         print("Incorrect")

# class Person :
#     def __init__(self , name , age):
#         self.name = name 
#         self.age = age 

#     def greet(self):
#         return "hello, " + self.name

#     def welcome (self):
#         message = self.greet()
#         print(message, "! Welcome to my Profile")

# p1 = Person("Abhi" , 19)
# p1.welcome()


# import numpy as np
# speed = np.array([20,43, 42, 64, 43,57,94,67,54])
# x = np.mean(speed)     ##mode
# y = np.median(speed)   ## median
# z = np.std(speed)      ## standard deviation
# w = np.var(speed)      ## variance
# q = np.percentile(speed , 40)  ##percentile 
# print(x)
# print(y)
# print(z)
# print(w)
# print(q)

# class Demo:
#     def __init__(self , name , age):
#         self.public_name = name
#         self.__private_age = age

#     def info(self):
#         print("My name is " + self.public_name + "and my age is " , self.__private_age)

# obj = Demo("Abhi" , 29)
# obj.info()
# # print(obj.public_name)       # ✔ Allowed
# # print(obj.__private_age)    # ❌ Error: private attribute

# import pickle

# class Student:
#     def __init__(self, name):
#         self.name = name

# # Store object in file
# s = Student("AIML Student")
# file = open("data.pkl", "wb")
# pickle.dump(s, file)
# file.close()

# # Load object from file
# file = open("data.pkl", "rb")
# obj = pickle.load(file)
# print(obj.name)
# file.close()


# class Animal:
#     def sound (self):
#         print("Animal makes sound")
# class Dog :
#     def sound (self):
#         print("Dog Barks")
# class Cat():
#     def sound (self):
#         print("Cats Meow")

# d = Dog()
# d.sound()

# c = Cat()
# c.sound()

# class Car :
#     def __init__ (self, b , model):
#         self.brand = b
#         self.model = model
#     def move (self):
#         print("Drive !")

# class Boat:
#     def __init__ (self , b , m):
#         self.brand = b
#         self.model = m
#     def move(self):
#         print("Drive !")

# class plane:
#     def __init__(self , b ,m):
#         self.brand = b
#         self.model = m
#     def move(self):
#         print("Fly !")

# c1 = Car("Ford" , "Mustang")
# b1 = Boat("Ibiza" , "Touring")
# p1 = plane("Boeing" , "747")

# for x in (c1 , b1 , p1):
#     x.move()

# class Vehicle:
#   def __init__(self, b, m):
#     self.brand = b
#     self.model = m

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

# class Number :
#     def __init__(self , n):
#         self.n = n
#     def __add__(self , other):
#         return self.n + other.n
# a = Number(10)
# b = Number(20)
# print(a+b)

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self):
#         return 3.14 * 5 * 5

# c = Circle()
# print(c.area())


# try:
#     a = int(input("Enter number: "))
#     print(10 / a)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Invalid Input!")
# finally:
#     print("Execution completed")

# class shape :
#     def __init__(self , l , w , r):
#         self.length = l
#         self.width = w
#         self.radius = r
#     def area(self):
#         pass

# class rectangle :
#     def area(self):
#         return self.length * self.width
    
# class circle :
#     def area(self):
#         return 3.14* (self.radius)**2
    
# s1 = shape(2 ,4, 2)
# for s1 in (rectangle , circle):
#     s1.area

# class 

# x = int (input("enter :"))
# n = int (input("enter :"))
# arr = []

a = int(input("start :"))
b = int(input("end :"))

def evennumbers (a,b):
    num = []
    for i in range (a,b):
        if i%2 == 0:
            num.append(i)
    print(num)
evennumbers(a,b)