# ===== Part 1 Lists =====
# question 1
fruits = ["apple", "banana", "coconut", "durian", "pineapple"]
print(fruits[2])    # third item
print(fruits[0])    # access from front
print(fruits[-1])   # access from behind

# question 2
fruits.append("mango")
fruits.append("grape")
print(fruits.pop(0))

# question 3
print(fruits[1:4])

# question 4
numbers = [n for n in range(1, 11)]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# question 5
nested_list = [fruits, numbers, even_numbers]
print(nested_list[1][1])

# ===== Part 2 Tuples =====
# question 1
integers = (1, 2, 3)
print(integers[1])

# question 2
# integers[2] = 4
# print(integers[2])

# question 3
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
result = (first_tuple + second_tuple) * 3
print(result)

# question 4
user_info = ("JIN ZICHENG", "21", "Wuhan")
name, age, city = user_info
print(name, age, city)

# ===== Part 3 Dictionaries =====
# question 1
students = {
    "JIN ZICHENG" : 0, 
    "Adam" : 80, 
    "Ben" : 70, 
    "Charlie" : 60, 
    "David" : 40
}
students["JIN ZICHENG"] = 90
print(students["JIN ZICHENG"])

# question 2
students["Emilia"] = 40  # add a new students
students["David"] = 50   # update a students
print(students["Emilia"], students["David"])

# question 3
print(students.keys())
print(students.values())
print(students.items())

# question 4
students.clear()
students = {
    "JIN ZICHENG" : {
        "age" : 21, 
        "grade" : 90
    }, 
    "Adam" : {
        "age" : 20, 
        "grade" : 80
    }, 
    "Ben" : {
        "age" : 20, 
        "grade" : 70
    }
}
print(students["JIN ZICHENG"]["grade"])

# question 5
square_numbers = {n : n ** 2 for n in range(1, 6)}
print(square_numbers)

# ===== Part 4 Mixed Data Structures =====
# question 1
student_info = {
    "JIN ZICHENG" : (
        ["Math", "English", "Physics", "Chemistry"], 
        [85, 100, 80, 95]
    )
}
print(student_info["JIN ZICHENG"])

# question 2
products = [
    {"name" : "apple", "price" : 2}, 
    {"name" : "banana", "price" : 4}, 
    {"name" : "egg", "price" : 1}, 
    {"name" : "carrot", "price" : 5}, 
    {"name" : "durian", "price" : 10}
]
products.sort(key=lambda x : x["price"])
print(products)

# question 3
employees = [
    {"name" : "Adam", "position" : "manager", "salary" : 2000}, 
    {"name" : "Ben", "position" : "worker", "salary" : 900},
    {"name" : "Charlie", "position" : "manager", "salary" : 2100}, 
    {"name" : "David", "position" : "worker", "salary" : 1200}, 
    {"name" : "Emilia", "position" : "worker", "salary" : 1500}
]

total_worker_salary = 0
worker_count = 0

for employee in employees: 
    if employee["position"] == "worker": 
        total_worker_salary += employee["salary"]
        worker_count += 1

average_worker_salary = total_worker_salary / worker_count

print(average_worker_salary)