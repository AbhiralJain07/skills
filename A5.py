# class Person :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = Person("Abhi" , 19)
# print(p1.name)
# print(p1.age)

# class Person :
    
#     def __init__(self,age):
#         self.age = age
# mukesh = Person(30)
# print(mukesh.age)

# rakesh = Person(32)
# print(rakesh.age)

# class Person:
#   def __init__(self, name, age, city, country):
#     self.name = name
#     self.age = age
#     self.city = city
#     self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name , p1.age)

# print(p1.city)
# print(p1.country)

# class Person :
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("hello , my name is ", self.name , ",my age is ", self.age)
# p1 = Person("Mukesh" , 23)
# p2 = Person("Rakesh" , 43)
# p1.greet()
# p2.greet()


## updatinfg value of attribute
# class Student :
#     def __init__(self , name , roll):
#         self.name = name 
#         self.roll = roll

#     def intro(self):
#         print("Name :", self.name )
#         print("roll :", self.roll)

# s1 = Student("abhi" ,23)
# s2 = Student("Om" ,20)

# s1.name = "NAMAN"
# s1.intro()
# s2.intro()


# class time:

#     def __init__(self ,h , m ,s):
#         self.hr = h
#         self.min = m
#         self.sec = s
    
#     # def adv_time(self , h , m ,s):
#     #     self.hr += h
#     #     self.min += m
#     #     self.sec += s

#     def display (self):
#         print ("time =", self.hr,":",self.min,":",self.sec)

# t = time(10,23,43)
# print("the time is :")
# t.display()

# class circle:
#     def __init__(self , r):
#         self.radius = r

#     def area(self):
#         return 3.14 * self.radius **2

#     def perimeter (self):
#         return 2*3.14*self.radius

# c1 = circle(2)

# print("area of circle :",c1.area())
# print("Perimeter of circle :", c1.perimeter())



# class bank:
#     def __init__(self , n , acc,bal,typ):
#         self.name = n
#         self.accNum = acc
#         self.bal = bal
#         self.typ = typ

#     def deposit(self):
#         amount = float(input("Enter amount to be deposited :"))
#         self.bal = self.bal + amount
#         print("Amount Deposited :",self.bal)

#     def withdraw(self):
#         amount = float(input("Enter amount to be withdraw :"))
#         if self.bal >= (amount+1000):
#             self.bal = self.bal - amount
#             print("\n You can Withdraw :",amount)
#         else:
#             print("\n Insufficient balance")

#     def display(self):
#         print("Account holder name :",self.name)
#         print("Account number",self.accNum)
#         print("Balance :",self.bal)
#         print("Account type :", self.typ)

# b1 = bank("Abhi", 832923 , 3822,"saving")
# b1.deposit()
# b1.withdraw()
# b1.display()


# class stack:

#     def __init__(self , max_size):
#         self.stack = []
#         self.max_size = max_size

#     def push(self , item):
#         def is_full():
#             return len(self.stack) == self.max_size
        
#         if is_full():
#             print("the Stack is full")
#         else:
#             self.stack.append(item)
#             print("Item Pushed")

#     def pop(self):
#         def is_empty():
#             return len(self.stack) == 0
        
#         if is_empty():
#             print("Stack is empty")
#             return None
#         else:
#             item = self.stack.pop()
#             print(item, "popped from stack")
#             return item
    
#     def display(self):
#         print("Current Stack :", self.stack)

# s = stack(10,20,23)
# s.display()

# class circle:

#     def __init__(self ,r):
#         self.radius = r

#     def get_radius(self):
#         print("radius :",self.radius)

#     def calc_area(self):
#         print("Area :", 3.14*self.radius**2)
# c1 = circle(5)
# c1.calc_area()
# c1.get_radius()

# class Car :
#     def __init__ (self , brand , model , manufacturing):
#         self.brand = brand
#         self.model = model
#         self.manufacture = manufacturing

#     def car_info(self):
#         print ("Car Brand :", self.brand , "\ncar Model :", self.model , "\nCar Manufaucturig Date :",self.manufacture)

# car1 = Car("Toyota" ,"Corolla" , 2025)
# car2 = Car("Suzuki" , "Swift", 2023)
# car3 = Car("Mahindra " , "Thar" ,2021)

# car1.car_info()



