# ============= PART 1 =============
# question 1
number = int(input("Please enter a number: "))
if number > 0:
    print("Positive number. ")
elif number == 0:
    print("It is zero. ")
else:
    print("Negative number. ")

# question 2
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("Even number. ")
else:
    print("Odd number. ")

# question 3
a, b, c = list(map(int, input("Please enter three numbers: ").split()))
result = max(a, b, c)
print(f"The largest number is {result}. ")

# question 4
year = int(input("Please enter the year: "))
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print("It is a leap year. ")
else:
    print("It is not a leap year. ")

# question 5
ch =  input("Please enter a alphabet: ")
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel. ")
    else:
        print("Consonant. ")
else:
    print("It is not a alphabet. ")

# question 6
score = float(input("Please enter student's score: "))
if score >= 90:     # assume A -> [90, 100]
    print("A")
elif score >= 80:   # assume B -> [80, 90)
    print("B")
elif score >= 70:   # assume C -> [70, 80)
    print("C")
elif score >= 60:   # assume D -> [60, 70)
    print("D")
else:               # assume F -> [0, 60)
    print("F")

# question 7
username = "apple"
password = "banana"

username_input = input("Please enter username: \n")
password_input = input("Please enter password: \n")

if username_input == username and password_input == password:
    print("Access granted. ")
else:
    print("Wrong username or password. ")

# question 8
number = int(input("Please enter a number: "))
if number in range(10, 51):
    print(True)
else:
    print(False)

# question 9
string = input("Please enter a string: ")
string_reverse = string[::-1]
if string_reverse == string:
    print("It is a palindrome. ")
else:
    print("It is not a palindrome. ")

# question 10
number = int(input("Please enter a number: "))
if number & 3 == 0 and number % 5 == 0:
    print(True)
else:
    print(False)

# ============= PART 2 =============
# question 1
for i in range(1, 11):
    print(i )

# question 2
number = int(input("Please enter a number: "))
for i in range(1, number + 1):
    print(f"{i} x {number} = {i * number}")

# question 3
n = int(input("Please enter the value of N: "))
sum = 0
for i in range(n + 1):
    sum += i
print(f"The sum of 1 to N is {sum}. ")

# question 4
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# question 5
number = int(input("Please enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}! = {factorial}")

# question 6
f_sequence = [1, 1]
for i in range(1, 9):
    f_sequence.append(f_sequence[i] + f_sequence[i - 1])
print(f_sequence)

# question 7
string = input("Please enter a string: ")
count = 0
for ch in string.lower():
    if ch in "aeiou":
        count += 1
print(f"There are {count} vowels in string. ")

# question 8
string = input("Please enter a string: ")
result = ""
for ch in string:
    result = ch + result
print(result)

# question 9
for i in range(6):
    print('*' * i)

# question 10
item_list = ["apple", "banana", "cherry", "durian"]
sum = ""
for item in item_list:
    sum += item
print(sum)

# ============= PART 3 =============
# question 1
number = 1
while number <= 10:
    print(number)
    number += 1

# question 2
number = input("Please enter a number: ")
sum = 0
i = 0
while i < len(number):
    sum += int(number[i])
    i += 1
print(sum)

# question 3
number = input("Please enter a number: ")
result = ""
i = 0
while i < len(number):
    result = number[i] + result
    i += 1
print(result)

# question 4
i = 1
while i * 7 <= 100:
    print(i * 7)
    i += 1

# question 5
number = input("Please enter a number: ")
while not number == "0":
    number = input("Please enter a number: ")

# question 6
number = input("Please enter a number: ")
digit = int(number[0])
i = 1
while i < len(number):
    digit = max(digit, int(number[i]))
    i += 1
print(digit)

# question 7
a, b = map(int, input("Please enter two numbers: ").split())

if a < b:
    a, b = b, a

remainder = 1
while not remainder == 0:
    remainder = a % b
    a = b
    b = remainder
print(f"The GCD of input is {a}. ")

# question 8
number = int(input("Please enter a number: "))
i = 0
while i * i <= number:
    if i * i == number:
        print("Perfect Square")
        break
    i += 1
else:
    print("Not perfect square")

# question 9
user_input = input()
while not user_input == "exit":
    user_input = input()

# question 10
number = int(input("Please enter a number: "))
i = 0
result = 0
while i <= number:
    result += i
    i += 2
print(f"Result = {result}")

# ============= PART 4 =============
# question 1
def question_1(num1, num2):
    return num1 + num2

# question 2
from math import sqrt
def question_2(number):
    i = 2
    while i < sqrt(number):
        if number % i == 0:
            return False
        i += 1
    else:
        return True
    
# question 3
def question_3(number):
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
    return result

# question 4
def question_4(string):
    return string[::-1]

# question 5
def question_5(number):
    if number % 2 == 0:
        print("The number is even. ")
    else:
        print("The number is odd. ")

# question 6
from math import pi
def question_6(radius):
    return pi * radius ** 2

# question 7
def question_7(celsius):
    return celsius * 1.8 + 32

# question 8
def question_8(string):
    count = 0
    for ch in string.lower():
        if ch in "aeiou":
            count += 1
    return count

# question 9
def question_9(num1, num2, num3):
    return max(num1, num2, num3)

# question 10
def question_10(number_list):
    sum = 0
    for number in number_list:
        sum += number
    return sum