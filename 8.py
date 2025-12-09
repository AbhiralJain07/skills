### OOPS

## class - is a blueprint for creating object

##creating class
# class Student:
#     name = "Abhiral"

# #creating object
# s1 = Student() 
# print(s1)

# s2 = Student()
# print(s2.name)  


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


### inheritance 

# class person:
#     def __init__(self , fname , lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname (self):
#         print(self.firstname , self.lastname)

# class student(person):
#     pass

# x = student("JOHN" , "DOE")
# x.printname()

class Animal :
    def __init__(self , speaks ):
        self.speak = speaks
    def printname(self):
        print(self.speaks)

class dog(Animal):
    pass

class cat(Animal):
    print("cat meows")

x = dog("barks")
x.printname()