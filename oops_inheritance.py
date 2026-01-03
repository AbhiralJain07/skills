#### <<<<<INHERITANCE>>>>>

## << MULTIPLE INHERITANCE
# class Employee :
#     company = "CTS"
#     name = "Abhi"
    
#     def show(self):
#         print(f"my name is {self.name } & I am working with {self.company}")

# class Coder :
#     language = "python"
#     def print_language(self):
#         print(f"I am learning {self.language}")

# class Programmer(Employee , Coder) :
#     company = "TCS"
#     def showlanguage(self):
#         print(f"The name is {self.company} & and he is good with {self.language}")

# a = Employee ()
# b = Programmer()

# b.show()
# b.print_language()
# b.showlanguage()


## <<< SINGLE INHERITANCE >>>
# class Employee :
#     company = "CTS"
#     name = "Abhi"
    
#     def show(self):
#         print(f"my name is {self.name } & I am working with {self.company}")

# class CODER (Employee):
#     language = "Python"
#     def show_language(self):
#         print(f"He is good at {self.language} so now he is working with {self.company}")

# a = Employee()
# b = CODER()

# b.show()
# b.show_language()

### << MULTI - LEVEL INHERITANCE >>

# class Admin:
#     a = 1

# class Manager(Admin):
#     b = 2

# class Member(Manager):
#     c = 3

# o = Admin()
# print(o.a)

# o = Manager()
# print(o.a , o.b)

# o = Member()
# print(o.c, o.b , o.a)