# print ("Press Enter to start the game!\n Press Ctrl+C to exit the game.")
# if input() == "":
#  while True:
#     print ("Welcome to the asbins game!")
#     number=int(input("Enter a number: "))
#     if number%2==0:
#         for i in range(3):
#             print ("Asbin")
#         print ("You win!")
#     else:
#         print ("You lose!")
#     print ("Press Enter to play again!\nPress Ctrl+C to exit the game.")
#     if input().lower()=="q":
#         break

# if input().lower()=="q":
#     print ("Thanks for playing!")

# from typing import List


# variable:str= "sdc"
# number:int= 5
# print (type(variable))
# print (type(number))

# fruits:list= ["apple", "banana", "cherry"]
# print (type(fruits))
# fruits:List[str]= ["apple", "banana", "cherry"]
# print (f'the type of fruits variable is: {type(fruits)}')

# age: int = 20
# print (f'the type of age variable is: {type(age)}')

# print(round(age/5), "is the result of dividing age by 5")

def get_name(name: str | None) -> str:
    if name is None:
        return "No name provided"
    else:
        return f"Hello, {name}!"
    

print(get_name("Alice"))
print(get_name(None))


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
person1 = Person("Bob", 30)
print(person1.greet())    
