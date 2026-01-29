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
# append method is used to add single element in lists
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
# print(x)

# Unpacking a tuple

fruits = ("apple","banana","cherry","strawberry", "watermelon", "starfruit")
#
# (green, orange, red) = fruits
#
# print(green)
# print(orange)
# print(red)

# adding a list of values the "tropic" variable:

# (green, *kalu, red) = fruits
#
# print(green)
# print(kalu)
# print(red)

# Python - Loop Tuples
# using for loop

# for x in thistuple:
#     print(x)

# Loop through the index numbers:
# for i in range(len(thistuple)):
#     print(thistuple[i])

# Using While - loop:
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i=i+1

# Joining two tuples
# tuple2 = (1,2,3)
# tuple3 = fruits+tuple2

# Multiplying tuple by 2

# tuple3 = fruits * 2
# print(tuple3)

# Tuple methods
# count() method

# print(fruits.count("apple")
# index() method
# print(fruits.index("apple"))

# Introducing Sets
# thisset = {"apple","banana","grapes","apple"}
# print(thisset)

# Sets are unordered, unchangeable and do not allow duplicate values
thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset) #True and 1 is considered the same
# false and 0 are considered the same

# Using len() function
# print(len(thisset))
# Using type int boolean string
# print(type(thisset))

# Using the set() constructor to make a set
# this_set = set(("apple","banana","grapes"))
# print(this_set)

# python - Access set items
# accses items looping through the sets using the for loops

thisset = {"apple","banana","grapes","watermelon"}
#
# for x in thisset:
#     print(x)

# Check if banana is present in the set - answrr in true and fakse
# print("banana" not in thisset)

# Change items - once a set is created you cannot change it but you can add new items.

# Adding Set items
# using add() methods

# thisset.add("orange")

# Add sets ,Use the update() method : Add any iterable
# update method is used to add two sets together and can also add
# list to the tuples
#
# tropical = ["pineapple","mango","papaya"]
# thisset.update(tropical)

# print(thisset)

# Remove set items
# To remove items from the set use remove() and discard() button
# thisset.discard("banana")
#  Using pop() method Sets are unordered so dont know which item will be removed

# x = thisset.pop()
# print(x)

# print(thisset)
