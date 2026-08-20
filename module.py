#module is a file that contains functions and classes that can be imported and used in other Python files.

def method_one(*args): #args is a tuple that contains all the arguments passed to the function. The *args syntax allows for an arbitrary number of arguments to be passed to the function.
    print("This is method one.", args if args else "No arguments provided.")

def method_two(**kargs): #kargs is a dictionary that contains all the keyword arguments passed to the function. The **kargs syntax allows for an arbitrary number of keyword arguments to be passed to the function.
    print("This is method two.", kargs if kargs else "No keyword arguments provided.")