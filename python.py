#variables and data types in python
# Integer
age = 25
# Float
height = 5.9
# String
name = "Alice"
# Boolean
is_student = True
# List
fruits = ["apple", "banana", "cherry"]
# Tuple
coordinates = (10.0, 20.0)
# Dictionary
person = {"name": "Bob", "age": 30}
# Set
unique_numbers = {1, 2, 3, 4, 5}
# Print variables
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)
print("Fruits:", fruits)
print("Coordinates:", coordinates)
print("Person:", person)
print("Unique Numbers:", unique_numbers)


# Check data types
print("Type of age:", type(age))
print("Type of height:", type(height))  
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))  
print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of person:", type(person))
print("Type of unique_numbers:", type(unique_numbers))

# Perform basic operations
sum_age_height = age + height
print("Sum of age and height:", sum_age_height)
fruits.append("date")
print("Updated Fruits:", fruits)
person["city"] = "New York"
print("Updated Person:", person)
unique_numbers.add(6)
print("Updated Unique Numbers:", unique_numbers)

# Accessing elements
first_fruit = fruits[0]
print("First fruit:", first_fruit)
person_name = person["name"]
print("Person's name:", person_name)
x_coordinate = coordinates[0]
print("X Coordinate:", x_coordinate)
is_five_in_set = 5 in unique_numbers
print("Is 5 in unique_numbers set?:", is_five_in_set)

# Looping through list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)


# Looping through dictionary
print("Person details:")
for key, value in person.items():
    print(f"{key}: {value}")

# Conditional statements
if age > 18:
    print("Adult")
else:
    print("Minor")


# Function to greet a person
def greet(person_name):
    return f"Hello, {person_name}!"
greeting = greet(name)
print(greeting)
# Function to calculate area of a rectangle
def calculate_area(length, width):
    return length * width
area = calculate_area(5, 3)
print("Area of rectangle:", area)

# Class definition for a simple Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
# Creating an instance of Person
person1 = Person("Charlie", 28)
introduction = person1.introduce()
print(introduction)





