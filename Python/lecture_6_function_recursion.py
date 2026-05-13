#                Functions & Recursion in python
# function is the block of statements that perform a spacific task.

# def sum_fun(a, b):
#   sum = a + b
#   print(sum)

# sum_fun(1,3)
# sum_fun(3,8)
# sum_fun(25,37)



# def Minus_fun(a,b):
#   return a+b


# Minus = Minus_fun(2,6)
# print(Minus)

#  avrage of 3 numbers
# def average(a,b,c):
#   sum = a+b+c
#   avr = sum / 3
#   print(avr)

# average(2,4,5)
# =================================================================================================
#                        function are two types
#  build-in function                                    user define function
#  print()                                            those fuc which are creating user
#  len()
#  type() 
#  range() 

# =================================================================================================
# Defult perameter: asigning a defulte value to perameter, which is used when no argumment is passed
#  for example:

# def multiply(a=6,b=6):# you can see default perameters in this line,(a,b=6) will work but (a=1,b) not working
#   mlp = a * b
#   print(mlp)

# multiply() # i wanna i will not pass any argument here but when i run it this show me error, for this purpose we can use default peramenter in the fisrt step.

# =================================================================================================
#            lets practice

# cities = ["peshawar", "islamAbad", "delhi", "chennai", "new Yourk"]

# def cities_len(cities):
#   length = len(cities)
#   print(length)

# cities_len(cities)



# cities = ["peshawar", "islamAbad", "delhi", "chennai", "new Yourk"]
# city = [ "delhi","islamAbad",   "new Yourk""peshawar","chennai",]

# def city_print(list):
#   for i in list:
#    print(i, end=" ")

# city_print(city)

# city_print(cities)
# def cal_fact(n):
#   fact=1
#   for i in range(1 , n+1):
#     fact *= i
#   print(fact)

# cal_fact(10000)



# def saspance(n):
#   fact = 1
#   for i in range(1, n+1):
#     fact *=i # 1,2, 6, 24, 120...
#   print(fact)

# saspance(4)

#  for today usd $ (1 usd = 280 rupees) convert to pkr using fun

# def converter(usd):
#   PKR = 280 * usd
#   print(usd, "USD = ", PKR)

# converter(100)


# def OddOREven(n):
#   if(n%2 == 0):
#     print("Even")
#   else:
#     print("Odd")

# OddOREven(535)

# =================================================================================================
#                Recursion: when a function call itself repeatedly work like loop
#  recursive function
# def recursion(n):
#  if(n == 0): # base case like in loops "stop"
#   return
#  print(n)
#  recursion(n-1) # call itself repeatedly
# recursion(5)


# def recursion(n):
#  if(n == 0):
#   return
#  n-=1
#  print(n)
#  recursion(n)
#  print("new")
# recursion(2)

# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   return n * fact(n-1)
# print(fact(3))

# def cal_sum(n):
#   if(n==0):
#     return 0
#   return cal_sum(n-1) + n
# sum =cal_sum(5)
# print(sum)
