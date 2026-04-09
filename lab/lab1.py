# ============== Part 1 ==============
# question 1
print("Welcome to Python Programming! ")

# question 2
print("Python is fun!\n"
      "Let's start learning Python. ")

# question 3
print(
    "He said, \"Python is amazing!\"\n"
    "This is line 1. \n"
    "\tThis is line 2 (with a tab space). "
    )

# question 4
language = "Python"
print(f"I am learning {language}! ")

# question 5
print("10\n20.5\n30")

# question 6
first_name = "John"
last_name = "Doe"
print(f"Hello, {first_name} {last_name}! Welcome to Python. ")

# question 7
print("Line1\n\tLine2\n\t\tLine3")

# question 8
name = "Alice"
age = 25
print(f"My name is {name}, and I am {age} years old. ")

# question 9
print("  *\n"
      " ***\n"
      "*****")

# question 10
print(5 + 3)
print(10 - 2)
print(4 * 6)
print(16 / 4)

# ============== Part 2 ==============
# question 1
name = "Alice"
age = 30
height = 5.7
is_student = True
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# question 2
x = 1
print(x)
x = 2
print(x)

# question 3
a = 8
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# question 4
x = 5
y = 10

x ^= y
y ^= x
x ^= y

print(x, y)

# question 5
is_python_fun = True
print(type(is_python_fun))

# question 6
list = ["a", "b", "c"]
print(list)
list[0] = "d"
print(list)

# question 7
dict = {
    "English":
        100,
    "Mathmatics":
        80,
    "Geography":
        70,
    "Chemistry":
        95
}
print(dict["Chemistry"])

# question 8
a = 10
b = "This is a str variable. "
b += str(a)
print(b)

# question 9
a = "This is a variable"
print(id(a))

# question 10
integer = 10
float = 2.34
string = "apple"
boolean = False
print(integer, type(integer))
print(float, type(float))
print(string, type(string))
print(boolean, type(boolean))

# ============== Part 3 ==============
# question 1
name = input("Please enter user name: ")
print(f"Hello, {name}! ")

# question 2
age = int(input("Please enter user age: "))
print(f"User age: {age}")

# question 3
first_name = input("Please enter first name: ")
last_name = input("Please enter last name: ")
print("User name:", first_name + " " + last_name)

# question 4
a, b = map(float, input("Please enter two numbers: ").strip().split())
print("The sum of numbers:", a + b)

# question 5
num = input("Please enter a number: ")
num = int(num)
print(f"The square of {num} is {num ** 2}")

# question 6
name = input("Please enter user name: ")
age = int(input("Please enter user age: "))
print(f"{name} is {age} years old. ")

# question 7
boolean = input("Please enter \"yes\" or \"no\": ").lower()
if boolean == "yes":
    boolean = True
elif boolean == "no":
    boolean = False
else:
    exit("Invalid input! ")
print(f"Input value = {boolean}")

# question 8
list = list(map(int, input("Please enter three numbers: ").strip().split()))
print(list)

# question 9
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"{number} is even. ")
else:
    print(f"{number} is odd. ")

# question 10
word = input("Please enter a word: ")
print(word.upper())
print(word.lower())
print(word[::-1])

# ============== Part 4 ==============
# question 1
a, b = map(int, input("Please enter two numbers: ").strip().split())
print(f"Result after addition: {a + b}")
print(f"Result after subtraction: {a - b}")
print(f"Result after multiplication: {a * b}")
if not b == 0:
    print(f"Result after division: {a / b}")
else:
    exit("Cannot divide by zero. ")

# question 2
number = int(input("Please enter a number: "))
print(f"Square of {number}: {number ** 2}")
print(f"Cube of {number}: {number ** 3}")

# question 3
a, b = map(int, input("Please enter two integers: ").strip().split())
if not b == 0:
    print(f"Floor division: {a // b}")
    print(f"Modulus: {a % b}")
else:
    exit("Cannot divide by zero! ")

# question 4
name = input("Please enter user name: ")
number = int(input("Please enter a number: "))
for i in range(0, number):
    print(name)

# question 5
from math import pi
radius = float(input("Please enter the radius: "))
print(f"The area of this circle is {pi * radius ** 2}")

# question 6
celsius = float(input("Please enter temperature in Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"Temperature in Fahrenheit is {fahrenheit}. ")

# question 7
obtained_mark = int(input("Please enter marks obtained: "))
total_mark = int(input("Please enter marks in total: "))
percentage = obtained_mark / total_mark * 100
print(f"The percentage of obtained marks is {percentage:.2f}%. ")

# question 8
principal = float(input("Please enter your principal: "))
rate = float(input("Please enter your interest rate: "))
time = float(input("Please enter your time of investment: "))
print(f"Your interest is {principal * rate * time}. ")

# question 9
a, b, c = list(map(int, input("Please enter three numbers: ").strip().split()))
print(f"The average of these three numbers is {(a + b + c) / 3}. ")

# question 10
total_days = int(input("Please enter time in days: "))
result_weeks = total_days // 7
result_days = total_days % 7
print(f"Time: {result_weeks} weeks {result_days} days. ")