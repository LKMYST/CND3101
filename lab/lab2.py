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
list = ["apple", "banana", "cherry", "durian"]
sum = ""
for item in list:
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
number = input()

# ============= PART 4 =============