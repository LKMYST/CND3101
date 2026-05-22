# ===== Question 1 =====
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Divide by zero!")
        return
    return a / b

def log(a, b):
    return math.log(a, b)

def pow(a, b):
    return math.pow(a, b)

