# import sys

# sys is a module that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. basically a interpreter information as a module

# print(sys.version)
# print(sys.version_info)
# print(sys.path)
# print(sys.executable)
# print(sys.platform)
# print(sys.maxsize)

"""This is multiple line comment"""

# print("""
# Practice of python programming

# Happy coding
# """)

# print("Hello World");print("Hello World");print("Hello World") # ; enables to write multiple statements in a single line

# print("Helloww", end=" ") # end is used to avoid new line after print statement
# print("Sandesh thapa") # end is used to avoid new line after print statement

# print(44)

# print("I am", 35, "years old.") # 35 is a int data type

# casting variable to a specific data type
# a = str(35) #casting int to string
# print("I am", a, "years old.") # 35 is a string data type

# #casting variable to a specific data type
# a = int("35") #casting string to int
# print("I am", a, "years old.") # 35 is a int data type

# a,b,c="Sandesh","Thapa",35 #multiple variable assignment
# print(a,b,c)


# fruits=["apple","banana","cherry"] #list
# x,y,z=fruits #unpacking list , tuple works the same
# print(x,y,z)

# def function1():
#     print("This is function 1")
#     global local_variable #turning local variable to global variable so that it can be accessed outside the function
#     local_variable = "This is local variable"

# function1()
# print(local_variable) #this will give error because local_variable is not defined in this scope

# import random
# print(random.random()) #generates random float number between 0 and 1


# name = "Sandesh Thapa   "

# for i in name:
#     print(i) #this will print each character of the string in a new line

# print("a" in name) #this will check if a is present in name or not and return True or False

# print ("x" not in name) #this will check if x is not present in name or not and return True or False

# print(name[:4]) #this will print first 4 characters of the string
# print(name[4:8]) #this will print characters from index 4 to index 8
# print(name[-4:]) #this will print last 4 characters of the string

# print(name.upper()) #this will convert string to uppercase
# print(name.lower()) #this will convert string to lowercase
# print(name.title()) #this will convert first character of each word to uppercase

# print(name.strip()) #this will remove any whitespace from the beginning or the end of the string

# x=9
# print(f"The value of x is {x:.2f}") #f-string is used to format string and it is available in python 3.6 and above

# print(name.encode()) #this will encode the string to bytes

# print(len(name)) #this will print the length of the string

# x=1 if "a" in name else 0 #this is a ternary operator which is used to assign value to a variable based on a condition

# identity operators

# print(x is y) #this will check if x is the same object as y and return True or False
# print(x is not y) #this will check if x is not the same object as y and return True or False

# membership operators

# print("a" in name) #this will check if a is present in name and return True or False
# print("a" not in name) #this will check if a is not present in name and return True or False

#dict
# data = {'name': "sandesh", 'age': 23, 'address': "chitwan"}

# for key,value in data.items():  # this will print the keys and values of the dictionary
#     if value==23:
#         print(key)  # this will print the key and value of the dictionary where value is 23

# print(data)  # this will print the dictionary
# print(type(data))  # this will print the type of the variable

# for key in data:  # this will print the keys of the dictionary
#     print(key)

# for value in data.values():  # this will print the values of the dictionary
#     print(value)

# for key, value in data.items():  # this will print the keys and values of the dictionary
#     print(key, value)    

# print("true" if "name" in data else "false")  # this will check if name is present in data keys and return true or false
# print("true") if "sandesh" in data.values() else print("false") # this will check if sandesh is present in data values and return true or false

# data.update({"name": "sandesh thapa"})  # this will update the value of name key
# print(data)

# data.pop("age")  # this will remove the age key from the dictionary
# print(data)

# data.clear()  # this will remove all the keys and values from the dictionary
# print(data)

# data.values()  # this will return the values of the dictionary
# print(data.values())

# data.keys()  # this will return the keys of the dictionary
# print(data.keys())

# data.items()  # this will return the keys and values of the dictionary as a list of tuples

# data.get("name")  # this will return the value of the name key

# data["name"]  # this will return the value of the name key

# # add the key value pair to the dictionary
# data["gender"] = "male"  # this will add the key gender with value male to the dictionary
# print(data)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear() #this will remove all the keys and values from the dictionary but the dictionary will still exist
# print(thisdict)
# del thisdict #this will delete the dictionary completely and it will not exist anymore
# print(thisdict)


# thisdict = [{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# },
# {
#     "brand": "Toyota",
#     "model": "Corolla",
#     "year": 2020
# },
# {
#     "brand": "Honda",
#     "model": "Civic",
#     "year": 2021
# }
# ]
# thisdict.pop("model") #this will remove the model key from the dictionary
# print(thisdict)


# thisdict.popitem() #this will remove the last inserted key-value pair from the dictionary
# print(thisdict)


# newdict=thisdict.fromkeys(("brand", "model", "year"), 0) #this will create a new dictionary with the keys from the tuple and the value as 0
# print(newdict)

#sets
# aset={"apple", "banana", "cherry"} #this is a set and it is unordered, unindexed, and does not allow duplicate values
# bset={"google", "microsoft", "apple"} #this is a set and it is unordered, unindexed, and does not allow duplicate values
# print(aset.intersection(bset)) #this will return the intersection of the two sets
# print(aset.difference(bset)) #this will return the difference of the two sets i.e Aset only
# print(bset.difference(aset)) #this will return the difference of the two sets i.e Bset only
# print(aset.union(bset)) #this will return the union of the two sets
# print(aset.issubset(bset)) #this will check if the first set is a subset of the second set and return True or False
# print(aset.issuperset(bset)) #this will check if the first set is a superset of the second set and return True or False
# print(aset.isdisjoint(bset)) #this will check if the two sets are disjoint and return True or False
# #add
# aset.add("microsoft") #this will add microsoft to the set
# print(aset)
# #remove
# aset.remove("apple") #this will remove apple from the set
# print(aset)
# #discard
# aset.discard("google") #this will remove google from the set
# print(aset)
# #pop
# aset.pop() #this will remove the last element from the set
# print(aset)
# #clear
# aset.clear() #this will clear the set
# print(aset)

""" random tip : think any data collection as a database and think any operation as a query and think any data as a table that means, any data collections should be able to CRUD (Create, Read, Update, Delete) which simply are as methods of the data collection, and also like in database, data collection should be able to perform operations like intersection, union, difference, subset, superset, disjoint etc. which are also methods of the data collection.
and also like in database other than crud , joins. There are search, filter and sort which are also methods of the data collection. so basically to have a simple understanding you can map any data collection as a database and any operation as a query and any data as a table.
"""


# groupby operation in thisdict based on the year key

# thisdict = [
#   {"brand": "Ford", "model": "Mustang", "year": 1964},
#   {"brand": "Toyota", "model": "Corolla", "year": 2020},
#   {"brand": "Honda", "model": "Civic", "year": 2021},
#   {"brand": "Toyota", "model": "Camry", "year": 2022},
#   {"brand": "Honda", "model": "Accord", "year": 2023},]

# from itertools import groupby

# grouped = groupby(thisdict, key=lambda x: x["year"])
# for key, value in grouped:
#     print(key, list(value))


#list

# from functools import reduce


# numbers = [1, 2, 3, 4, 5]
# fruits = [ "banana", "cherry","apple", "mango", "kiwi", "orange", "grape"]

#crud

#add
# numbers.append(6) #this will add 6 to the list at the end
# print(numbers)
# #remove
# numbers.remove(2) #this will remove 2 from the list
# print(numbers)
# #insert
# numbers.insert(2, 7) #this will insert 7 at index 2
# print(numbers)
# #pop
# numbers.pop() #this will remove the last element from the list
# print(numbers)
# #clear
# numbers.clear() #this will clear the list
# print(numbers)

# #other operations in list
# #sort
# numbers.sort() #this will sort the list in ascending order if list is numbers and in alphabetical order if list is string
# print(numbers)
# #reverse
# numbers.reverse() #this will reverse the list
# print(numbers)
# #count
# print(numbers.count(1)) #this will count the number of 1 in the list
# #copy
# newlist = numbers.copy() #this will copy the list
# print(newlist)

# #list comprehension
# newlist = [x for x in range(10)] #this will create a list of numbers from 0 to 9
# print(newlist)
# newlist = [x for x in range(10) if x % 2 == 0] #this will create a list of even numbers from 0 to 9
# print(newlist)

# #generator expression
# newlist = (x for x in range(10)) #this will create a generator expression of numbers from 0 to 9
# print(newlist)
# newlist = (x for x in range(10) if x % 2 == 0) #this will create a generator expression of even numbers from 0 to 9
# print(newlist)

# #map and filters
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)
# product = reduce(lambda x, y: x * y, numbers)
# print(product)


# a=1
# b=lambda x: x**2
# print(b(a))


#lambda function is an anonymous function which can take any number of arguments but can only have one expression. It is used when we need a small function for a short period of time and we don't want to give it a name. It is also used when we want to pass a function as an argument to another function. and it also can be used as callback function in built in functions like map, filter, reduce

# a lambda function i.e lambda x: x**2 is a function that takes one argument x and returns x squared is equal to def function1(x):
#     return x**2

# def check_even(number):
#     return number % 2 == 0

# newList=list(map( lambda x: x**2, numbers)) #this will create a list of numbers squared
# print(newList) #this will print the list

# filteredList=list(filter(check_even, numbers)) #this will create a list of even numbers from the newList
# print(filteredList) #this will print the list

# newList=list(map( lambda x: x%2==0, numbers)) #this will create a list of boolean values indicating even numbers
# print(newList) #this will print the list

# fruits_uppercase=list(map(lambda x: x.upper(), fruits)) #this will create a list of fruits in uppercase
# print(fruits_uppercase) #this will print the list

#conditional statements
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

# #ternary operator
# print("a is greater than b") if a > b else  print("b is greater than a") if b > a else print("a and b are equal")

# for x in range(3):
#   print(x)

numbers=[5,7,2,9,1,3]
# print the greatest number in the list
# filter the greater number than first value in the list and if there are remove smaller one and kepe on filtering unitll len is 1 and print the last remaining number

# for i in range(len(numbers)-1):
#     numbers = list(filter(lambda x: x > numbers[0], numbers))
#     if len(numbers) == 1:
#         break
# print(numbers[0])


# check first two numbers in the list and if first number is greater than second number then remove second number from the list and if second number is greater than first number then remove first number from the list and keep on checking unitl len is 1 and print the last remaining number

# for i in range(len(numbers)-1):
#     if numbers[0] > numbers[1]:
#         numbers.pop(1)
#     else:
#         numbers.pop(0)
#     if len(numbers) == 1:
#         break
# print(numbers[0])


# def find_greatest_number(numbers:list):
#     for i in range(len(numbers)-1):
#         if numbers[0] > numbers[1]:
#             numbers.pop(1)
#         else:
#             numbers.pop(0)
#         if len(numbers) == 1:
#             break
#     return numbers[0]


# print(find_greatest_number(numbers))

""" Types of Error and Error Handling in Python.
Error Types:
1. Syntax Error: This occurs when the code is not written in the correct syntax of the programming language. For example, missing a colon at the end of an if statement or using an undefined variable.
2. Name Error: This occurs when a variable or function is not defined in the current scope. For example, trying to access a variable that has not been declared or calling a function that does not exist.
3. Type Error: This occurs when an operation is performed on a variable of the wrong type. For example, trying to add a string and an integer or calling a method that is not applicable to the variable's type.
4. Value Error: This occurs when a function receives an argument of the correct type but an invalid value. For example, trying to convert a string to an integer that is not a number.
5. ZeroDivisionError: This occurs when trying to divide a number by zero.
6. IndexError: This occurs when trying to access an index of a list that is out of range.
7. KeyError: This occurs when trying to access a key in a dictionary that does not exist.
8. AttributeError: This occurs when trying to access an attribute of an object that does not exist.
9. ImportError: This occurs when trying to import a module that does not exist.
10. ModuleNotFoundError: This occurs when trying to import a module that does not exist.
11. OSError: This occurs when an operation on a file or directory fails due to an operating system error.
12. FileNotFoundError: This occurs when trying to access a file that does not exist.
13. KeyboardInterrupt: This occurs when the user interrupts the execution of a program using the keyboard.
14. MemoryError: This occurs when the interpreter runs out of memory.
15. RecursionError: This occurs when the interpreter runs out of stack space.


Error Handling:
Error handling in Python is a way to handle errors that occur during the execution of a program. It is a way to prevent the program from crashing and to provide a better error message to the user.
Error handling in Python is done using try and except blocks.

try:
  # code that may raise an error
except Exception as e:
  # code to handle the error
  print(f"An error occurred: {e}")

"""

# # handle error specifically using try and except block
# try:
#     # code that may raise an error
#     x = 1 / 0
# except ZeroDivisionError as e:
#     # code to handle the error
#     print(f"An error occurred: {e}")
# finally:
#     # code that will always execute
#     print("This will always execute")


# # handle error universally using try and except block
# try:
#     # code that may raise an error
#     x = 1 / 0
# except Exception as e:
#     # code to handle the error
#     print(f"An error occurred: {e}")
# finally:
#     # code that will always execute
#     print("This will always execute")

# #raising error using raise keyword
# # raise ValueError("This is a value error") #this will raise a value error with the message "This is a value error"

# try:
#     a=3
#     b=2
#     if a>b:
#         raise ValueError("a is greater than b") #this will raise a value error with the message "a is greater than b"
#     else:
#         print("b is greater than a")
# except ValueError as e:
#     print(f"An error occurred: {e}")

# cars=["Ford", "Volvo", "BMW"]

# def get_car(cars):
#     for i in cars:
#         yield i #yield is used to return a generator object which can be iterated over and it is used to create a generator function which can be used to create an iterator object

# cars=get_car(cars) #this will return a generator object which can be iterated over

# print(next(cars)) #this will return the first value of the generator object
# print(next(cars)) #this will return the second value of the generator object
# print(next(cars)) #this will return the third value of the generator object

# from core import Codyasbin 

# codyasbin = Codyasbin()
# print(codyasbin.description) #this will print the description of codyasbin.description



