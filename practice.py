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


