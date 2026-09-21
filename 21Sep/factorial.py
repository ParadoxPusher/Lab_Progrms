def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in range(6):
    print(f"{i}! = {factorial(i)}")