#           Lesson 1 in Python About Lists or Arrey
# Lists and Arrey are same in Prog.

# Lists: A build-in data types that stores set of values,
# it can store elements in deff data types {int, str, float...}

# lists = [1,3,4,3.3,54,54,"43", "haris"]
# print(lists) # 1,3,4,3.3,54,54,"43", "haris"
# print(lists[0]) #1
# print(type(lists)) # list

#===========================================================================
#                  Lesson 2 in Python  Slicing in Lists same as str
#  Lists and string are almost Same but one defferent which is
# 1. lists: are Mutible(changeble). we can change values in it
# 2. String: are Immutible(unchangeble). we can not change values in it

# str = "hares"
# str[3]= "i" # cannot changing
# print(str)


# Lists = [1,3,4,3.3,54,54,"43", "haris"]
# Lists[7] = "khan" # will changing
# print(Lists)

# Lists = [1,3,4,3.3,54,54,"43", "haris"]
# list = Lists[0:5]
# list1 = Lists[3:7]
# list2 = Lists[-7:]
# print(list)
# print(list1)
# print(list2)

#===========================================================================
#                  Lesson 3 in Python Mothods for only Lists

# list = [1,3,2,4,5,3]
# list.append(4) # Add an elm at end of list
# list.sort() # show elm in ascending order like 1,2,3
# list.sort(reverse=True) # show elm descending order like 3,2,1,
# list.reverse() # reverce list like 3,1,2
# list.insert(0, 6) # insertion of in elm (idx, elm)
# list.remove(5) # remove elm which is occurse in lists
# list.pop(0) # remove elm with idx
# print(list)

#===========================================================================
#                Lesson 4 in Python  Tuples
# tuple slicing is same like list and str
#  lists and tupls are same but tuples is immutible like str and instead [Square brakets] use (prenthises)

# top = (1,2,3,4,5) # tuples
# top[2] = "haris" # not changing will show error
# print(top)
# print(type(top))

#===========================================================================
#               Lesson 5 in Python  Tuples methods

# tup = (1,2,5,4,5)
# tup1 =tup.index(5) # return index of first occuranse
# tup2 =tup.count(5) # count elm occurse in tuple
# print(tup1)
# print(tup2)

#===========================================================================
#                 Let Practice 6 in Python
# Prac:1  write a prog to ask the user to enter the name of your 3 favorite movies & store in list
# list = []
# Movie1 = input("enter your 1st favorite movie : ")
# Movie2 = input("enter your 2nd favorite movie : ")
# Movie3 = input("enter your 1rd favorite movie : ")

# list.append(Movie1)
# list.append(Movie2)
# list.append(Movie3)

# print(list)

# Prac:2 write a prog to check if list contains a polindrome  of elm. (hint use copy())
# polindrome: those elm which is read correctly from both start and end like "racear", ma'am.

# str = ["ma'ma"]
# str1 =  str.copy() # 1,2,3,3,2,1
# str1.reverse()

# if(str == str1):
#   print("polindrome")
# else:
#   print("Absolutly Not")


# Prac:3 write a prog to count the num of students with the A, B, C.. Grades.

# tup = ("A", "D", "B","A", 'C', 'D', 'B','C',"A")

# tup1 = tup.count("A")
# tup2 = tup.count("B")
# tup3 = tup.count("C")
# tup4 = tup.count("D")
# print(tup1)
# print(tup2)
# print(tup3)
# print(tup4)


# Prac:4 write a prog to mske a list with descending order and sort them in ascending order
# list = []
# tup = ["A", "D", "B","A", 'C', 'D', 'B','C',"A"]
# tup.sort()

# print(tup)

