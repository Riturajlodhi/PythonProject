# print("Hello everyone we are learning Python")
# num = 10
# print(num)
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name,age) """
from random import setstate

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

# clear() method empties the set
# thisset.clear()
# print(thisset)

# Loop sets using for loop

# for x in thisset:
#     print(x)

# Joining sets
# Union() method unite two sets together both update and union does the same thing
# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {"John","Bananas","carrot"}

#
# set3 = set1.union(set2)
# print(set3)

# Use | to join two sets
# set5 = set1 | set2 | set3
# print(set4)

# Joining a set and a Tuple
# x = {"a", "b", "c"}
# y = (1,2,3)
#
# z = x.union(y)
# print(z)
# Note: The | operator only allows you to join sets with sets, and not with other data types like you can with the union() method.

# Update :- metho inserts all items from one set into
# print(another)
#Intersection() method only shows the duplicates
set1 = {"a","b","c"}
set2 = {1, 2, 3, "a"}

# set3 = set1.intersection(set2)
# Using & operator instead of intersection
# set3 = set1 & set2
# without using the third variable but will change original set
# set1.intersection_update(set2)
# print(set1)

# Difference method - Keep all items from set1 that are not present in set2
# set3 = set1.difference(set2)
# using - to join two sets
# set3 = set1 - set2
# print(set3)

# difference_update() without using
# set1.difference_update(set2)
# print(set1)

# Symmetric_difference() or use ^ operator
# set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2
# print(set3)

# symmetric_difference_update() method keep the items that are not present in both setstate
# set1.symmetric_difference_update(set2)
# print(set1)
# removes all the duplicates and returns the rest in the sets
# Python frozenset - immutable version of a set.
"""like sets it contains unique,unordered,unchangeable elements
Unlike sets, elements cannot be added or removed from a frozenset."""

# x = frozenset({"apple","banana","cherry"})

# print(x)
# print(type(x))
# isdisjoint() Returns whether two frozensets have an intersection

a = frozenset({1,2})
# b = frozenset({3,4})
# print(a.isdisjoint(b))
# return true none of items are present are present in both sets

# issubset() or <= / <  returns True if this frozenset is a (proper) subset of another

g = frozenset({1,2,6})
# print(a.issubset(g))
# print(a <=g)
# print(a < g)
# print(g.issuperset(a))
# print(g > a)
# print(g >= a)

# Union unites the frozenset without any duplication duplicate values
# print(a.union(g))
# print(a | g)

# update() method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x.update(y)
# x|=y
# print(x)
# print(x)

# x.symmetric_difference_update(y)
# x ^= y

# Using remove or discard method in sets to remove a value from the sets
# x.remove("banana")

# Using add() method to add items in set
# x.add("orange")
# print(x)

# Dictionary use to store key:value pairs
# Dictionary items are ordered, changeable, and do not allow duplicates
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)

#Printing the brand value of the dictionary
# print(thisdict["brand"])
# Dictionaries are changeable
# Duplicate values not allowed in Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
# print(thisdict)

# using the len function we can measure the length of thee dictionary
# the class type of dictionary is dict

# The dict() method to make a dictionary:
# thisdict = dict(name= "Raj", age = 52, country = "africa")
# print(thisdict)

# get the values of key values using get method
# print(thisdict.get("model"))

# Get keys
# x = thisdict.keys()
# print(x)
# changing the key values
# thisdict["brand"]="tata"
# print(thisdict)

# Get Values
# print(thisdict.values())

# Adding  a new key value pair
# x = thisdict.values()
# print(x) #before the change
# thisdict["color"] = "red"

# print(x) #after the change
# print(thisdict)

# Get a list of the key:value
# print(thisdict.items())

# Check if key exists

# if "color" in thisdict:
#     print("yes, 'color' is one of the keys in the thisdict dictionary")

# Update Dictionary update()
# thisdict.update({"color":"black"})
# print(thisdict)

# Add items
# thisdict["country"]= "france"
# print(thisdict)

# using update() method
# thisdict.update({"color":"violet"})
# print(thisdict)

# Remove Dictionary Items
# using pop() method :-

# thisdict.pop("year")
# Using del method
# del thisdict["model"]
# print(thisdict)

# del method is also used to delete the dictionary

# clear() method empties the dictionary

# Loop Dictionaries

# for x in thisdict:
#     print(x)

# print(thisdict[x])
# Using values() method

# Using values method to return values of a dictionary
# for x in thisdict.values():
#     print(x)

# Using keys() method to return keys
# for x in thisdict.keys():
#     print(x)

# Using items() method to loop through both keys and values:
# for x,y in thisdict.items():
#     print(x,y)

# Copy Dictionaries
mydict = thisdict.copy()
print(mydict)

# Nested Dictionaries
"""
myclass = {
    "child1" : {
        "name": "gutla",
        "year": 2003
    },
    "child2" : {
        "name": "Tabar",
        "year": 2001
    },
    "child3" : {
        "name": "badnaam",
        "year": 2011
    }
}
"""
# print(myclass)
# or we can create first three different dictionaries and then create a dictionary and put all three in one dictionary
#
"""
class4 = {
    "name" : "linus",
    "year" : 2005

}
class7 = {
    "name" : "kailash",
    "age" : 20
}

myschool = {
    "class4": class4,
    "class7": class7
}
"""
# print(myschool)

# loop through Nested Dictionaries
# using items() method

# Access items in Nested Dictionaries
# print(myschool["class4"]["year"])

# for x,obj in myschool.items():
#     print(x)
#     for y in obj:
#         print(y + ':', obj[y])

# popitem() - removes the last item
# class4.popitem()
# print(class4)

# ___________________________________________________
# Python Conditions and If statements

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
"""
# if keyword
a = 33
b = 23
if a > b:
     print("b is greater than a")
"""
# Using boolean variable:
# is_logged_in = True
# if is_logged_in:
#     print("Welcome back!")

# Python Elif statement
"""
a = 45
b=56
if a > b:   
    print("a is greater than b")
elif a <= b:
    print("a is less than or equal to b")
    """

# Multiple elif conditions
"""
score = 75

if score >= 90:
    print("grade A")
elif score >= 80:
    print("grade B")
elif score >= 70:
    print("grade c")
elif score >= 60:
    print("grade d")
"""
# categorizing age groups
"""
age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")
"""
# Python Else Statement

# The else keyword
"""
a = 200
b = 3
if b>a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")
    
"""
num = 7
# if num % 2 == 0:
    # print("The number is even")
# else:
    # print("The number is odd")

# _______________
# conditional_statement

# Check even or odd numbers
"""
num = 7
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
"""
# temperature = 28
#
# if temperature > 30:
#     print("It's hot outside!")
# elif temperature > 20:
#     print("It's warm outside")
# elif temperature > 10:
#     print("It's cool outside")
# else:
#     print("It's cold outside!")

# Else as fallback
"""
username = "apple"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")
"""
# Shorthand if - one line if statement
a=74
b=9
# You still need colon: after the condition
# if a > b:print("a is greater than b")

# Short Hand If..Else
# One-line if/else that prints a value:
# print("A") if a>b else print("B")

# Assign a value with if...else one line if else
#
# a = 10
# b = 20
# bigger = a if a > b else b
# print("Bigger is", bigger)
# variable = value_if_true if condition else value_if_false

# Multiple conditions on One line

# b = 82
# a = 63
# print("A") if a > b else print("=") if a==b else print("B")
"""
# Finding the maximum of two numbers
x = 12
y = 21
max_value = x if x>y else y
print("Maximum value:", max_value)
"""
# setting a default value
username = ""
display_name = username if username else "guest"
# print("Welcome,", display_name)

# Shorthand is only for quick simple assignment

# Python logical Operators
"""
and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
"""
# The and Operator
# a=89
# b=65
# c=92
# if a>b and c>a:
#     print("both conditions are true")

# The or operator
"""
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
"""
# The not Operator
# a=4
# b=9
# if not a > b:
#     print("a is not greater than b")

# Combining multiple Operators
"""
age = 58
is_student = False
has_discount_code = True

if (age < 18 or age > 25) and not is_student or has_discount_code:
    print("Discount applies!")

# not false = true
Operator Precedence -- parenthesis > not > and > or

"""
"""
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities")
"""
"""
username = "Lenovo"
password = "password"
is_verified = True

if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")
    """
"""
# Nested if Statements
x = 41
if x > 10:
    print("Above 10")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20")
else:
  print("You are too young to drive")
    """
"""
score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but low attendance")
    else:
        print("Pass but low attendance")
else:
    print("fail")
"""
# a = 32
# b = 25
#
# if a > b:
#     pass
#     print("Score processed")

# Pass with multiple Conditions
# value = 50
#
# if value < 0:
#     print("Negative value")
# elif value == 0:
#     pass
# else:
#     print("Positive value")

# Python match statement
"""
day = 9
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("good day")
        using _ operator as last option 
        """
# Combine values
# Use pipe character | as an or operator in the case evaluation to check for more than one value
"""
day = 4
match day:
    case 1|2|3|4|5:
        print("Today is a weekday")
    case 6|7:
        print("I love weekends!")
    case _:
        print("No match")
    """
# Python While loops
# using break to stop the follow of the loop
# using continue
# i = 1
# while i<10:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# continue statement -- it will skip 3
"""
i = 0
while i < 6:
    i += 1
    if i==3:
        continue
    print(i)
"""
# the else block will not be executed if the loop is stopped by a break statement

# For loop

fruits = ["apple", "banana","cherry"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)
#
    # The break Statement in for loop
"""
for x in fruits:
    print(x)
    if x == "banana":
        break

# the continue statement in for loop

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range() function
for x in range(6):
    print(x)

# range(5) means 0 to 4 not o to 5

   # Herer using the start parameter
for x in range(2,6):
    print(x)

    # Increment by 3
for x in range(2,10,3):
    print(x)

    # Else in for loop
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

    # Nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

"""
# sari sari raat aho me bharta
# for x in [0,1,2]:
    # pass

# Python Functions
# a functions is a block of code which only runs when it is called
# a function can return data as a result
# a function helps avoiding code repetition
"""
# creating a functiom usinf def function
def my_function():
 print("Hello from a function")
 # calling a function
my_function()
my_function()

# function name :- start with a letter or underscore
# a function can only contain letters, numbers, and underscores
# function names are case sensitive(myFunction and myfunction are different)

temp1 = 77
celcius1 = (temp1 - 32) * 5/9
print(celcius1)

temp2 = 95
celcius2 = (temp2 - 32) * 5/9
print(celcius2)

# this is the repetition of code but with functions - reusable code

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32)* 5/9

print(fahrenheit_to_celcius(77))
print(fahrenheit_to_celcius(52))

# Return values
def greet():
    return "Hello from function"

message = greet()
print(message)

def function():
    pass # no error will come

"""
# ____________________________________________________


# object oriented proprogramimg language in python

# oops used to structure your code - provides structure to your code , make code easier to maintain
# keep your code dry , allows you to build reusable applications with less code

# Classes and Objects

# class Myclass:
    # x = 5

# creating object p1 and printing the value of x:
# p1 = MyClass()
# print(p1.x)

# delete Objects
# del p1

# Multiple objects
# p1 = Myclass()
# p2 = Myclass()
# p3 = Myclass()
#
# print(p1.x)
# print(p2.x)
# print(p3.x)

# the pass statement
# class person:
    # pass

# The _init_() Method :-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# p1 = Person("Rahul", 36)
# print(p1.name)
# print(p1.age)

# Creating a class without __init__():
"""
class person:
 pass
p1 = person()
p1.name = "swami"
p1.age = 31

print(p1.name)
print(p1.age)
"""
# Multiple Parameters

class Person:
    def __init__(self,name,age,city,country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
