import re

# ===== question 1 =====
text = "Visit https://www.example.com or http://test.org for more info."

website_regex = re.compile(r"https?://[^\s]+")  # [^\s] refers to not-space content
output = website_regex.findall(text)

print(output)

# ===== question 2 =====
text = "Some color codes: #FF5733, #123, #1A2B3C, #XYZ123"

color_regex = re.compile(r"#(?:[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})")
output = color_regex.findall(text)

print(output)

# ===== question 3 =====
text = 'Look at that cool book and the letter.'

words = re.findall(r"\w+", text)
output = [w for w in words if re.search(r"(\w)\1", w)]

print(output)

# ===== question 4 =====
text = 'She said "hello world" and then "goodbye".'

quote_words_regex = re.compile(r'"[^"]*"')
output = quote_words_regex.findall(text)

print(output)

# ===== question 5 =====
text = "Valid dates: 2023-12-01, 2024-02-30, 2023-00-10, 2023-11-31"

# first filter
date_regex = re.compile(r"\d{4}-(?:0[1-9]|1[012])-(?:0[1-9]|[12]\d|3[01])")
dates = date_regex.findall(text)

output = []

# second filter
for d in dates:
    matches = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
    year, month, day = map(int, matches.groups())

    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if month == 2:
        if day <= 28 or (is_leap_year and day == 29):
            output.append(d)
    elif month in [4, 6, 9, 11]:
        if day <= 30:
            output.append(d)
    else:
        output.append(d)

print(output)

# ===== question 6 =====
text = "Anna saw a radar and met Hannah at noon."

words = re.findall(r"\w\w+", text)  # abort single alphabet
output = [w for w in words if w[0].lower() == w[len(w) - 1].lower()]

print(output)

# ===== question 7 =====
text = "<div>Hello <b>world</b>!</div>"

html_regex = re.compile(r"<[^>]+>") # [^>] refers to not '>' content
output = html_regex.sub("", text)

print(output)

# ===== question 8 =====
text = "This is is a test test of regex regex."

repeat_regex = re.compile(r"\b(\w+) \1\b", re.IGNORECASE)
output = repeat_regex.findall(text)

print(output)

# ===== question 9 =====
text = "Files: report.txt, data.csv, image.png, notes.log"

file_regex = re.compile(r"\w+\.\w{3}")
output = file_regex.findall(text)

print(output)

# ===== question 10 =====
text = "'user_1', '1user', 'user-name', 'valid_user123'"

# find all names
username_list = re.findall(r"'([^']+)'", text)
# select valid names
output = [
    u for u in username_list
    if re.fullmatch(r"[A-Za-z0-9_]{5,15}", u)   # no space in {5,15}
]

print(output)