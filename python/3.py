### >>>> list and tupples



#LIST - ek mutable{jiski value change ho skti hai} data type hota hai
# list mai hmeshha square bracket use hota hai
# marks = [93.3 , 94.4 , 89.4 , 74.5 , 66.6]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[3])

# student = ["karan" , 89.4 , 19 , "from Delhi"]
# print(student)
# student[0] = "arjun"
# print(student)

# # slicing is mai bhi possible hai
# marks = [87,64,33,95,76]
# print(marks[1:4])
# print(marks[3:8])
# print(marks[ :3])
# -ve index mai bhi sliciing ho jati hai

# list method
# list = [2,4,5,4]
# list = ["banana" , "apple"  , "litchi"]##jb yeh use krenge tab append wala function nhi kam krega
# list.append(3)
# list.sort()
# list.sort(reverse=True)
# list.reverse()
# list.insert(3,8)
# list.remove("apple")
# print(list)

#append method - list ke aakhiri mai jo bhi number chahe add kr skte hai
#sorting method - list ko sahi order mai sort kr dena 
#jb bhi ye dono sath mai lgayenge tab list sort hokr aayegi
# reverse=True ye lgane se list dscending order mai arrange ho jaati hai
#list.insert(index,element)
##jb bhi ye function lgayenge tab jobhi index jo bhi number chahte ho tab vo lag jayega
#remove function se list mai jo bhi number repeat ho rha hai vo remove ho jayega


# TUPPLES - immutable{jiski value change na ho} data type hota hai
# #isme hmesha parenthesis use hota hai
# #tupple mai value change nhi hoti hai

# tup = (2,1,3,1)
# print(type(tup))
# print(tup[2])

# tup  = (1)
# print(tup)
# print(type(tup))

# tup = (9.0)
# print(tup)
# print(type(tup))

# tup = ("abhiral" ,)
# print(tup)
# print(type(tup))

# tup = ("abhiral" )
# print(tup)
# print(type(tup))

# tup = (3 ,)
# print(tup)
# print(type(tup))

# #slicing in tupple
# tup = (1,2,3,2)
# print(tup[1:3])
# print(tup.index(2))# return index of first occurence
# print(tup.count(2))#counts total occurence of element

# movies =[]
# movie1 = "3 idiots"
# movie2 = "YJHD"
# movie3 = "JK"

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

# # #OR we can write code as

# movies = []
# movie = input("enter 1st movie")
# movie = input("enter 2nd movie")
# movie = input("enter 3rd movie")

# movies.append(movie)
# movies.append(movie)
# movies.append(movie)

# print(movies)

# #OR aise bhi likh skte hai

# movies = []
# movie = input("enter 1st movie")
# movies.append(movie)
# movie = input("enter 2nd movie")
# movies.append(movie)
# movie = input("enter 3rd movie")
# movies.append(movie)
# print(movies)
  

# grade = ["C" , "D" , "A" , "B" , "A" , "A" ]
# print(grade.sort())



# list = [ "i"]
# print(list)
# list.insert(0 ,"e ")
# print(list)
# list.remove(0, "e" )
# print(list)
# list.append("e")
# print(list)
# list.sort()
# print(list)
# list.pop()
# print(list)
# list.reverse()
# print(list)

# n = int (input("Enter number :\n"))
# i = 1
# for i in range(1,n):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")   
#     else :
#         print(i) 
            