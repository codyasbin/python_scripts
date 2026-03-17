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