import re

# question 1
text = "There are 25 apples and 30 bananas."
output = re.findall(r"\d+", text)
print(output)

# question 2
text = "Python is fun to learn!"
output = re.findall(r"\w+", text)
print(output)


# question 3
text = "This is a sample sentence."
output = re.findall(r"\s+", text)
print(len(output))

# question 4
text = "Hello, how are you?"
output = re.match(r"^Hello", text)
print(bool(output))

# question 5
text = "Welcome to the new world"
output = re.search(r"world$", text)
print(bool(output))

# question 6
text = "Regular expressions are powerful."
output = re.findall(r"[aeiou]", text)
print(output)

# question 7
text = "John and Alice are friends with Bob."
output = re.findall(r"[A-Z][a-z]+", text)
print(output)

# question 8
text = "This test finds four word size."
output = re.findall(r"\b\w{4}\b", text)
print(output)

# question 9
text = "My cat and dog are playing together."
output = re.search(r"(cat|dog)", text)
print(output)

# question 10
text = "My SSN is 123-45-6789."
output = re.search(r"\d{3}-\d{2}-\d{4}", text)
print(output)