#                    while and for Loops
#  Loops are used to repeat the instruction

#                                  while loop

# count = 10  # iterater
# while count <=  20:
#   print("hello", count)   # this processes which is work in circle form called iteration
#   count += 1

# i = 0
# while i <= 100:
#   print(i)
#   i+=1

# print("Loop Ended")

# i = 5
# while i >= 0:
#   print(i)
#   i-=1
#   print("Loop Ended")


# i = 1 # 1 < 100
# while i <= 100 : # 5 < 6 print (5)  5-=1 = 4 3 2 1 0 -1 -2 -3// -11, -10
#   print(i)
#   i+=1

# count = 100 # 100 > 1
# while count > 0:
#   print(count)
#   count -=1

# math table forming
# n = int(input("Enter a num : "))
# i = 1
# while i <= 10:
#   print(n*i)
#   i +=1

# list = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(list): # = 9
#   print(list[idx])
#   idx +=1

# list = ["haris", "khan", "mohmandi", "tayyab", "amad", "ruhullah", "bilal", "asif"]

# idx = 0

# while idx < len(list): # 8
#   print(list[idx])
#   idx +=1

# tuple = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Search a num in tuple : "))
# idx = 0
# while idx < len(tuple):
#   if(tuple[idx] == x):
#     print("num has found")
#   else:
#      print("finding...")
#   idx +=1



#                 BREAK AND QUENTINUE
# BREAK
# tuple = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Search a num in tuple : "))
# idx = 0
# while idx < len(tuple):
#   if(tuple[idx] == x):
#     print("num has found")
#     break # use to terminate(torna) the loop when encountered
#   else:
#      print("finding...")
#   idx +=1

# QUENTINUE

# i = 1
# while i <= 10:
#   if(i==3):
#     i+=1
#     continue # ues for skip this value
#   print(i)
#   i+=1


# i = 1
# while i <= 10:
#   if(i % 2 == 0):
#     i+=1
#     continue # ues for skip this value
#   print("new", i)
#   i+=1

#===========================================================================


#                                for Loops in python
#  Loops are for sequencial traversal.for traversing strs lists and tuples
# nums = [1,2,3,4,5,3,2,6,1,7,8,9]

# for val in nums:
#   print(val)


# Vagitable = ("potatoes", "tomatoes", "bananas", "mango", "orange")

# for val in Vagitable:
#   print(val)
# else:
#   print("END") # we can use here else

#===========================================================================
#                    Lets Practice

# nums = [1,2,3,4,5,3,2,6,1,7,8,9]

# for val in nums:
#   print(val)



# nums = [1,2,3,4,5,3,2,6,1,7,8,9]
# x = int(input("Enter : "))
# idx = 0
# for val in nums:
#   if(val == x):
#     print("num found at idx", idx, "which is ", val )
#   idx +=1

#===========================================================================
#                       range() in python
#  range function returns a sequence of numbers, starting from 0 default and increament by 1 by default. and stop before a specified number.

# req = range(5)
# for val in req:
#   print(val) # 0 to 4


# for val in range(5): # range(stop)
#   print(val)

# for val in range(1,10): # range(start,stop)
#   print(val)

# for val in range(1,10,2): # range(start,stop,step)
#   print(val)


#        Even num up to 100 using range method
# for val in range(0, 100, 2):
#   print(val)

#        Odd num up to 100 using range method
# for val in range(1, 100, 2):
#   print(val)

# for i in range(100, 0, -1):   #start from 100 and endind is 0, and step -1 will work like, from 100 -1 = 99 -1 98...
#   print(i)

#        math table using range
# n =int(input("Enter : "))

# for val in range(0, 11):
#   print(val * n)


#                          PASS key
# for val in range(10): # if ues want to pass empty loop you should use pass key word othervise will show error
#   pass


#              for loop
# n = int(input("Enter : ")) # 4
# sum = 0 # 1, 3, 6, 10
# for i in range(1, n+1):
#   sum +=i
# print(sum) # 1, 3, 6, 10


# n = 3
# sum = 0
# for i in range(1, n+1):
#   sum +=i
# print(sum)

#     while loop for plus the all num to given num
# n = int(input("Enter : ")) # 3
# i= 1 # 2
# sum = 0 # 1, 3
# while i <= n:
#   sum +=i # 1, 3,
#   i+=1 # 2, 3, 4
# print(sum ) # 1, 3, 6


#     while loop  for factorial of a num
# n = int(input("Enter : ")) # 3
# i= 1
# sum = 1
# while i <= n:
#   sum *= i
#   i+=1
# print(sum )

#       for loop  for factorial of a num


# n = int(input("Enter : "))
# sum = 1
# for i in range(1, n+1):
#   sum *=i
#   i +=1
# print(sum)


#     ENDING OF LOOPS
#===========================================================================

