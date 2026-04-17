import re

# question 1
text = "Visit https://www.example.com or http://test.org for more info."
output = re.findall(r"https?://[^\s]+", text)
print(output)

# question 2
text = "Some color codes: #FF5733, #123, #1A2B3C, #XYZ123"
output = re.findall(r"#(?:[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})", text)
print(output)

# question 3
