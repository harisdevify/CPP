#                Lesson 1 in Python    Dictionry and Object are same
# Dictionary are use to Store data values in key:values pairs they are unordred and muttable, and not allow's duplicate key.
#  sets are mutable but elms in set are immutable

# Dic = {
#   "name":"haris",
#   "age":21,
#   "matric Pass": True,
#   "Job":"Web Dev",
#   "Subjects": ["Dic", "ste", "some more"],
#   "class": ("govt collage", "1st Year", "D5 room" )
# }
# print(type(Dic))
# print(Dic["name"]) # accesing to value
# Dic["name"] = "Mohmandi" # will change the first name
# print(Dic)

#===========================================================================
#                  Lesson 2 in Python   Nisted Dictionary

# Dic = {
#   "name":"haris",
#   "age":21,
#   "Subjects_Marks": {
#     "math": 97,
#     "chem":98,
#     "physics":99
#   }
# }
# print(Dic["Subjects_Marks"]["math"]) # accesing nisted Dictionary

#===========================================================================
#                  Lesson 3 in Python   Methods for Dictionary
# Dic = {
#   "name":"haris",
#   "age":21,
#   "Subjects_Marks": {
#     "math": 97,
#     "chem":98,
#     "physics":99
#   }
# }
# Dic.keys() # return the all Keys in Dic
# Dic.values() # return the all values in Dic
# Dic.items() # return all keys & values pairs as tuple
# Dic.get("name") # return the value using get mathod is best practice instead of Dic["name"].
# Dic.update({"city":"peshawar", "New_city": "ghalania"}) # new key:value add at Dic
# print(Dic)

#===========================================================================
#           Lesson 4 in python     Sets
#The Collaction of unordered items, Each item in the set must be unique and immutible.
# set = {1,2,1,2,2,"world", "world",4}
# print(set) # 1,2,4,'world'.  the repeated items will be stored only once.
# print(len(set)) # 4
# print(type(set)) # set

#===========================================================================
#           Lesson 5 in python   Methods for Sets
# set = {1,2,2,2,"world", "world",4, "haris","mohmandi"}
# set.add("haris") # add an elm at set
# set.clear() # clear set
# set.remove("world") # remove given elm
# set.pop()# remove a random values
# print(set)


#               Union and Intersection

#  Union:  Combines both sets values and return new axcept duplication
# Intersection: Combines Common values
# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.union(set2)) # 1,2,3,4
# print(set1.intersection(set2)) # 2,3

#===========================================================================
#                Lets Practice  in Python
# prac:1  store the words meaning in dictionary
# Dictionary = {
#   "table":[
#     "a Piece of furnature",
#     "list of facts and figures"
#   ],
# "cat": "a small animle"
# }
# print(Dictionary)


# sets = {"pyhton", "java", "c++", "python", "c", "java", "javaScript", "c++", "python", "javaScript" } # 10
# print(len(sets)) # will print 6 instead 10, because  the repeated items will be stored only once.

# prac:2  write a program to enter marks of 3 subjects from the user and them in dectionary, start with an empty dectionary and add one by one. use subjects as a key and marks as value.

# marks = {}
# x = int(input("enter your marks : "))
# marks.update({"Math": x})
# x = int(input("enter your marks : "))
# marks.update({"physics": x})
# x = int(input("enter your marks : "))
# marks.update({"Chemistry": x})
# print(marks)


# set = {9,9.0}
# set = {9, "9.0"} #1 possible to show 9 and 9.0
# set = {
#   ("float", 9),("int", 9.0) #2 possible solution
# }
# print(set)
