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