import re

# question 1
text = "There are 25 apples and 30 bananas."
output = re.findall(r"\d+", text)
print(output)