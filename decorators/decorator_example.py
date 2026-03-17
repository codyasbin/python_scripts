#without decorator

def greet(func):
    print ("sir name is: ", func())

    
def name(name="sandesh"):
    return name

print (greet(name))


#with decorator
@greet
def sir_name():
    sir_name="magar"
    return sir_name

# decorators are a powerful tool in Python that allow you to modify the behavior of functions or classes. They are often used to add functionality to existing code without modifying the original code directly. In this example, we have a simple decorator called `greet` that takes a function as an argument and prints the result of calling that function. The `name` function is defined to return a string, and when we call `greet(name)`, it executes the `name` function and prints the result.