### >>>> dict and set

#dict is also mutable
#there is unordered in dictionaries(inshort index)
#dicitionaries don't allow duplicate keys (inshort : repeat nhi krte)
info = {
    "reg no." : "24BAI10677",
    "name" : "Abhiral",
    "learning" : "coding",
    "subject" : "python",
    "topic" : "dictionaries and sets",
    "age" : 19,
    "is adult"  : True,
    "marks" : 94.4,
    12.99  :94.4
}
# print(info) #isme sari info jo bhi store ki hai hai vo sab show krega
# print(info["topic"])#isme topic ko specify krke btayega 

info["name"] = "abhi"  #overwrite hojayega short mai 
info["surname"] = "jain" #aisa krne se add bhi ho jayega jo bhi apan chahte hai
print(info)


# null_dict = {}
# null_dict["name"] = "abhiral"
# print(null_dict)

###>>>Nested dictionary
# student = {
#     "name" : "abhiral jain",
#     "marks" : {
#         "comp phy" : 91,
#         "discrete" : 89 ,
#         "evs" : 96 ,
#     }
# }
# print(student) #isme student ki details run ho jayengi 
# print(student["marks"]) #isme student ke specific marks run ho kr aayenge
# print(student["marks"]["comp phy"]) #isme student ke specific subjects ke marks run ho jayenge


###dictionary methods,
# student = {
#     "name" : "abhiral jain",
#     "marks" : {
#         "comp phy" : 91,
#         "discrete" : 89 ,
#         "evs" : 96 ,
#     }
# }

# print(student.keys()) #jo bhi outer layer wali keys hai vo print kr ke aati hai
# print(list(student.keys())) #list ke form mai aa jaygi
# print(len(list(student.keys()))) #isse student ke list ki lenth ka pta chalega 
# print(student.values())  #returs all values
# print(student.items()) #return all key values in tupple form
# print(student.get("name")) #jo bhi info chahiye usse get kr do
# print(student("name2")) #error aa jayega
# print(student.get("name2"))# no error -->> none aa jayega 
# student.update({"city" : "bhopal"})
# print(student) ###yha pr update kr dega dictionary mai


####>>>sets in python<<<<

#set is collection of unordered items
#each element is the set must be unique and immutable
#set ke andar list aur dictionary store nhi ho skti
## list ur dict ko set ke andar store nhi kra skte kyunki dono mutable hoti hai
## set to muatble hai lekin set ke andar ke elements immutable hai 


# collection = {1,2,3,4 ,"hellooo" , 5}
# collection1 = {1,2,2,2,2,"hellooo" , 5}

# print(collection)
# print(collection1)
# print(type(collection))
# print(len(collection))   ##>>>len total number of items 
# print(len(collection1))   ##>>>isme len sirf 4 hi hogi kyunki set mai duplicate values ki koi value nhi hoti


###how to create empty set
# collection2 = set()
# print(type(collection2))

##set method
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("hello")
# collection.add((1,2,3))  #ye tupple hai
# collection.remove(1)
# collection.clear()

# print(collection)
# print(len(collection))

# collection4 = {"hello" , "coding" ,"Abhiral jain" , "python"}

# print(collection4.pop())  ##>>popm se ye hoga ki value apne aap pop ho jaati hai

# collection5 = {"hello" , "coding" ,"Abhiral jain" , "python",1,3,2}
# collection = {1,2,4,6,6}

# print(collection5.union(collection)) ##>>>combines both set values and returns new
# print(collection5.intersection(collection)) ####>>>combines common values and returns new


#practice problem
##1>
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a peice of furniture" , "list of facts and figures"]
# }

# print(dictionary)

#Q2>>
# subjects = {
#     "python" , "java" , "c++" , "python" , "javascript",
#     "java" , "python" , "java" , "c++" , "c"
# } 
# print(subjects)
# print(len(subjects))

#Q3>>>
# marks = {}
# x = int(input("enter phy marks :"))
# marks.update({"phy" : x})

# x = int(input("enter chem marks :"))
# marks.update({"chem" : x})

# x = int(input("enter phy marks :"))
# marks.update({"math" : x})

# print(marks)

# print(len(marks))


#Q4>>>>
# values = {9,9.0 , 8 , 8.0}
# print(values) ##aise mai python result mai 9 ki vlaue hi print krega 
# #kyunki pythin 9 aur 9.0 ko ek hi vlaue manta hai
# # ab agr 9 aur 9.0 ko store krna hai to hame 9.0 ko string bnana padega

# values1 = {"9" , 9.0}
# print(values1)

# values2 = {
#     ("float" , 9.0),
#     ("int" , 9) 
# }

# print(values2)

