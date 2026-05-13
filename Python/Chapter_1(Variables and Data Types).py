#          Prictice 1 in Python  PRINT FUNCTION

# print(input("name : "))  complex method

# name = input("name :")   simple method
# age = int(input("Age :"))
# price = float(input("Price :"))
# print("my name is ",name, "my age is", age, "my book price is", price)

#===========================================================================

#          Prictice 2 in Python CONDITION and if nested condiyion is valid

# age = 17
# if(age >= 18):
    # if(age>= 80):
    #   print("can not vot")
    # else:
    #    print("Can vote")
#   print("you can vote")  #  Indentation (proper spacing) like look start in it line
# else:
#  print("you can not vote")

#==============================================================================================


#          Prictice 3 in Python CONDITION

# Light = input("Put Trafick Color :")

# if(Light == "Red"):
#   print("Stop")
# elif(Light == "Green"):
#   print("Go")
# elif(Light == "Yellow"):
#   print("Look")
# else:
#   print("Light is Broken")

#==============================================================================================


#          Prictice 4 in Python  CONDITION

# marks = int(input("marks : "))

# if(marks >= 90):
#   print("A+ Grade and Very Good")
# elif(marks >= 80 and marks < 90):
#   print("B Grade and Good")
# elif(marks >= 70 and marks < 80  ):
#   print("C Grade and Poor")
# else:
#   print("D Grad and Fial")

#==============================================================================================


# Some Important About Logical  "OR( || ) " and " AND (&&)"

#   AND                              ===                                     OR
# T T = T                            ===                                   T T = T
# T F = F                            ===                                   T F = T
# F T = F                            ===                                   F T = T
# F F = F                            ===                                   F F = F

#==============================================================================================



#          Prictice 5 in Python   INLINE CONDITIONS OR TERNARY OPRATERS

# exp 1
# food = input("food :")

# eat = "Yes" if food == "Apple" else "No"
# print(eat)

# exp 2
# food = input("food : ")

# print("Sweet")  if food == 'jalebi' or food == 'Cack' else print("Not Sweet")




#==============================================================================================
#       Prictice 6 in Python CLEVER IF / TERNARY OPRATERS
#  exp 1
# age = int(input("Enter your Age : "))

# vote = ("Yes","No") [age <= 18]
# print(vote)

#  exp 2
# salery = int(input("Salery : "))

# salery = salery*(0.1, 0.2) [salery >= 50000 ]
# print(salery)

#==============================================================================================
#       Prictice 7 in Python  OPERATERS

#1 Arithmetic operaters
#  +, -, /, *, %, **

#2 Comperision operaters
# ==,!=,>,<, >=, <=

#3 Assigmwnt operaters
# =,+=,-=, *=, /=, %=, **=

#4 Logical operaters
# &&, ||, !, AND, NOT, OR

#===========================================================================
#Prictice 8 in Python  Data Type Conversion

#1 Conversion (automaticly convert)
#2 Casting(manually)


#     Conversion

# a = 1
# b = 2.30
# c = a+b
# here a is automaticly convert to float 1.00
# print(c)

# Casting

# a = float(1)
# b = int("2")
# c = str(1)
# print(type(a) , type(b), type(c))
#  here value of data is manually is converted

#===========================================================================
#                Prictice 9 in Python    INPUT()

# name = input("Enter Your name : ")
# print("wellcome", name)


# age = int(input("Enter Your age : "))
# print("your age is ", age)

# Book_Price = float(input("Enter Your name : "))
# print("The Book Price is", Book_Price)

#===========================================================================
#                Prictice 10 in Python   Let Practice
# QUESTION:      write a Program to input 2 nums and print their sum

# firstQ = int(input("Enter Your First Num : "))
# SecondQ =int( input("Enter Your Second Num : "))

# print("Sum is :",firstQ +SecondQ )

#===========================================================================
#                Prictice 11 in Python   Let Practice
# QUESTION:   write a program to input side of a square and input its area

# a = float(input("Enter side of square : "))

# print("Area of the square is:", a**2, a*a)

#===========================================================================
#                Prictice 12 in Python   Let Practice
# QUESTION: write a program input 2 floating point nums & print their average

# a = float(input("Enter 1st num : "))
# b = float(input("Enter 2nd num : "))
# c = (a + b) / 2
# print("the average of two num is :", c)

#===========================================================================
#                Prictice 13 in Python   Let Practice
# QUESTION: write a program input 2 int nums a and b, print true if a is >= b, if not print false

# a = int(input("Enter 1st num : "))
# b = int(input("Enter 2nd num : "))

# print(a>= b)
