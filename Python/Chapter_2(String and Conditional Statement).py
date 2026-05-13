

#          Prictice 1 in Python  STRING
# str1 ="this is my first str "
# str2 ="this is my 2nd str "
# str3 ="this is my 3rd str "

# print(str1 + str2 + str3)
# print(len(str1))
# print(len(str1 +" "+str2 + str3))

#===========================================================================
#          Prictice 2 in Python  Indexing (position in String)

# using var[] for index
# str = "apna collage"
# str1= str[5]
# print(str1)

#===========================================================================
#          Prictice 3 in Python   slicing(tukry karna)
# Accessing part of a string using var[from:to]

# str = "apna collage"
# str1 = str[5:12]
# str2 = str[0:len(str)] # will print to end
# str3 = str[0:]  # will print to end
# str4 = str[:12] # will print to start
# print(str1)
# print(str2)
# print(str3)
# print(str4)


#  here we can also use -ve num for slicing like -1, -2, -3...
# str = "apna collage"
#    ...-5-4,-3,-2,-1
# str1 = str[-12:]
# print(str1)
#===========================================================================
#         Prictice 4 in Python   String Functions

# fun 1:  endswith("substr"): return true if string end is with substr
# str = "i m learing python from apna collage"
# str1 = str.endswith("age")
# print(str1)

# fun 2: capitalize(): capitle 1st char in str
# str = "i am learing python from apna collage"
# str1 = str.capitalize()
# print(str1)

# fun 3: replace(old, new): replce a word
# str = "i am learing python from apna collage"
# str1 = str.replace("python", "javaScript")
# print(str1)

# fun:4: find(): search a word in str
# str = "i am learing python from apna collage"
# str1 = str.find("python")
# print(str1)

# fun:5: count(): find how many time exist given word in your str
# str = "i am learing python from apna collage"
# str1 = str.count("python")
# print(str1)

#===========================================================================
#                Practice 5   Let Practice

# prac:1  write a prog to inp users first name & print thier len

# name = input("Enter Your First name : ")
# nameLen = len(name)
# print(nameLen)

# prac:2 write a prog to find the occurance(maujod hona) of a "$" in str

# str = "i am learing python $ from apna collage"
# str1 = str.count("$")
# print(str1)

# prac:3 write a prog to chack if a num entered by a user is odd or even

# str = int(input("Enter your Num : "))

# if(str % 2  == 0):   # exp 20 % 2 = 0
#   print("The Given num is Even")
# else:
#   print("The Given num is Odd")

# prac:4 write a prog to find greatest 3 nums entered by users

# a = int(input("Enter your a Num : "))
# b = int(input("Enter your b Num : "))
# c = int(input("Enter your c Num : "))

# if(a >= b and a >= c):
#   print("a num is largest ",a)
# elif(b >= c):
#   print("b num is largest ",b)
# else:
#   print("c num is largest ",c)

# prac:5 write a prog to chick if entered num is multiple of 7 or not

# str = int(input("enter a num : "))
# num = str % 5
# if(num == 0 ):
#   print("Yes")
# else:
#   print("No")
