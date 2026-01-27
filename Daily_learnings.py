# print("Hello everyone we are learning Python")
# num = 10
# print(num)
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name,age) """

# sorting Lists
""" def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

def func(n):
  return abs(n - 30)

thislist = [90, 45, 84, 73, 28]
thislist.sort(key = func)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.upper)
print(thislist)
"""
"""
 # copying lists using copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# using list method
my_list  = list(thislist)
print(my_list)

#using : operator
Mylist = thislist[:]
print(Mylist)

#Joining lists
#join two list 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
"""
#Append list2 to list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
#
# for x in list2:
#     list1.append(x)

# print(list1)
# list1.extend(list2)
# print(list1)

# Working with tuples
# Accessing tuples values
thistuple = ("apple", "banana", "watermelon", "guava", "kiwi", "jackfruit")
# print(thistuple[1])

# negative indexing
# print(thistuple[-1])

# Range of indexes
# print(thistuple[:4])
# print(thistuple[2:])

# Check if items present exists
# if "apple" in thistuple:
#     print("Yes, apple is in thistuple")

# Python - Update tuples
# tuples are unchangeable and immutable
# changing them into lists vice verse

x = ("apple", "banana", "grapes", "guava")
# y = list(x)
# y[-2] = "kiwi"
# x = tuple(y)
# print(x)
# y.append("orange")
# x = tuple(y)
# print(x)

# Removing items in a tuple
# Tuples are unchangeable convert it to list and then again to tuple
# y.remove("grapes")
# x = tuple(y)
# print(x)

# Deleting the tuple
# del x
print(x)