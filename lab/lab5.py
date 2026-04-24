# ===== question 1 =====
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)
print(len(numbers))
numbers.remove(3)
print(numbers)

# ===== question 2 =====
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[:3])
print(fruits[-2:])
print(fruits[1:4])

# ===== question 3 =====
squares = [i ** 2 for i in range(1, 11)]
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(squares)
print(even_squares)

# ===== question 4 =====
list1 = [3, 7, 1, 9]
list2 = [2, 6, 8, 4]
list1.sort()
list2.sort()
sorted_list = list1 + list2
print(sorted_list)

# ===== question 5 =====
mixed_list = [123, 34, 4.56, 78.9, "apple", "banana"]
mixed_list = [x for x in mixed_list if not isinstance(x, int)]
print(mixed_list)
mixed_list.append("Python")
print(mixed_list)