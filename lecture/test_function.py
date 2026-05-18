def max(num1:int, num2:int, num3:int)->int:
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max

def sum(numbers:list)->int:
    sum = 0
    for n in numbers:
        sum += n
    return sum

def in_range(num:int, start, end)->bool:
    return num in range(start, end)

print(max(3, 1, 2))
print(sum([8, 2, 3, 0, 7]))
print(in_range(3, 1, 10))
