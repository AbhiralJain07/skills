# class Employee:
#     language = "python"
#     salary =120000

#     def getInfo(self):
#         print ("The language is " , self.language , "and the salary is" , self.salary)

#     @staticmethod
#     def greet():
#         print("Good Morning")

# harry = Employee()
# harry.name = "Abhiral"
# harry.getInfo()
# harry.greet()

### constructor 

# class Employee:
#     def __init__(self , n , l , s):
#         self.name = n 
#         self.language = l
#         self.salary = s
#         print(" constructor is also known as dunder method")

#     def getInfo(self):
#         print("my name is" , self.name , "and i am learning" , self.language , "also my salary is" , self.salary)

# abhiral = Employee("Abhiral" , "Python" , 120000)
# abhiral.getInfo()


### practice set

# class Programmer : 
#     company = "Microsoft"
#     def __init__(self , n , s , p):
#         self.name = n
#         self.salary = s
#         self.pincode = p

# p = Programmer("Abhiral" , 120000 , 462001)
# print(p.name , p.salary , p.pincode , p.company) 

# p = Programmer("Rohan" , 120000 , 462001)
# print(p.name , p.salary , p.pincode , p.company) 

# class Calculator :
#     def __init__(self , n):
#         self.n = n

#     def sqr(self):
#         print("the square of the number is" , self.n*self.n)
         
#     def cube(self):
#         print("the cube of the number is" , self.n*self.n*self.n)

#     def sqrroot(self):
#         print("the square of the number is" , self.n**1/2)

# a = Calculator(4)
# a.sqr()
# a.cube()
# a.sqrroot()

