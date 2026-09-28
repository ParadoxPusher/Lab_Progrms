def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2              
    return wrapper

@double_result
def add(a, b):
    return a + b

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(f"Doubled result: {add(a, b)}")