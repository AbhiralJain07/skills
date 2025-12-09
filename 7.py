## <<<<< FILE HANDLING. >>>>>>##

## reading a file

# a = open("myfile.txt" , "r")
# text = a.read()
# print(text)
# a.close()

## writing a file

# f = open("myfile.txt" , "w")
# f.write("HELLO WORLD !!")
# f.close()

## append a file :

# f = open("myfile.txt" , "a")
# f.write("HELLO WORLD !!")
# f.close()


## using a readline() method :

# f = open("myfile.txt" , "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

## using a writeline() method

# f = open("myfile2.txt" ,"r")
# i =0
# while True:
#     i =i +1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in maths is :", m1)
#     print(f"Marks of student {i} in OS is :", m2)
#     print(f"Marks of student {i} in DSA is :", m3)


## using a seek() method
with open ("myfile3.txt" , "r") as f:
    ##move to 10th byte in file
    f.seek(10)

    ## move next 5 bytes
    data = f.read(5)
    print(data)