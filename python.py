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

# Inheritance example
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} My student ID is {self.student_id}."

# Creating an instance of Student
student1 = Student("Diana", 22, "S12345")
student_introduction = student1.introduce()    
print(student_introduction)


# Exception handling example
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")


# File operations example
file_path = "example.txt"
# Writing to a file
with open(file_path, "w") as file:
    file.write("Hello, World!\nThis is a sample file.")


# Reading from a file
with open(file_path, "r") as file:
    content = file.read()
    print("File content:")
    print(content)
# Clean up the created file
import os   
os.remove(file_path)

# Importing and using a standard library module
import math
circle_radius = 7
circle_area = math.pi * (circle_radius ** 2)
print("Area of circle with radius", circle_radius, "is:", circle_area)
# Using datetime module to get current date and time
from datetime import datetime
current_datetime = datetime.now()
print("Current date and time:", current_datetime)
# Using random module to generate a random number
import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)
# Using os module to get current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)
# Using sys module to get Python version
import sys
python_version = sys.version
print("Python version:", python_version)
# Using json module to serialize and deserialize data
import json
data = {"name": "Eve", "age": 29, "city": "Los Angeles"}
json_data = json.dumps(data)
print("JSON data:", json_data)
parsed_data = json.loads(json_data)
print("Parsed data:", parsed_data)
# Using collections module to create a counter
from collections import Counter
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
item_counter = Counter(items)
print("Item counts:", item_counter)
# Using itertools module to create combinations
from itertools import combinations
comb = combinations(['A', 'B', 'C'], 2)
print("Combinations of 2 from ['A', 'B', 'C']:", list(comb))
# Using re module for regular expressions
import re
pattern = r'\b\w{3}\b'
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print("3-letter words in the text:", matches)
# Using subprocess module to run a simple command
import subprocess
result = subprocess.run(['echo', 'Hello from subprocess'], capture_output=True, text=True)
print("Subprocess output:", result.stdout)
# Using time module to measure execution time
import time
start_time = time.time()
time.sleep(1)  # Simulate a delay
end_time = time.time()
execution_time = end_time - start_time
print("Execution time (seconds):", execution_time)
# Using hashlib module to create a hash
import hashlib
hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print("SHA-256 hash of 'Hello World':", hex_dig)
# Using base64 module to encode and decode data
import base64
original_data = b'Python is fun!'
encoded_data = base64.b64encode(original_data)
decoded_data = base64.b64decode(encoded_data)
print("Original data:", original_data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
# Using urllib module to make a simple HTTP request
import urllib.request
response = urllib.request.urlopen('http://www.example.com')
html_content = response.read()
print("HTML content from example.com (first 100 characters):", html_content[:100])
# Using xml.etree.ElementTree module to parse XML data
import xml.etree.ElementTree as ET
xml_data = '''<root>
    <child name="child1">Value1</child>
    <child name="child2">Value2</child>
</root>'''
root = ET.fromstring(xml_data)
for child in root:
    print(f"Child name: {child.attrib['name']}, Child value: {child.text}")
# Using csv module to read and write CSV data
import csv
csv_file_path = 'example.csv'
# Writing to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'Los Angeles'])
# Reading from a CSV file
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV Row:", row)
# Clean up the created CSV file
os.remove(csv_file_path)
# Using shutil module to copy a file
import shutil
source_file = 'source.txt'
destination_file = 'destination.txt'
# Create a source file
with open(source_file, 'w') as file:
    file.write("This is the source file.")
# Copy the source file to destination
shutil.copy(source_file, destination_file)
print(f"Copied {source_file} to {destination_file}")
# Clean up the created files
os.remove(source_file)
os.remove(destination_file)
# Using threading module to create a simple thread
import threading
def print_numbers():
    for i in range(5):
        print("Number:", i)
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
print("Thread has finished execution.")


# Advanced python concepts 
# List comprehension
squares = [x**2 for x in range(10)]
print("Squares from 0 to 9:", squares)
# Generator expression
cubes = (x**3 for x in range(10))
print("Cubes from 0 to 9:", list(cubes))
# Lambda function
add = lambda a, b: a + b
print("Sum of 3 and 5 using lambda:", add(3, 5))
# Map function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers using map:", doubled)
# Filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)
# Reduce function