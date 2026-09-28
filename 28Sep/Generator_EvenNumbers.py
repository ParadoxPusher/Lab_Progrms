def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

print("Even numbers up to 10:")
for num in even_numbers(10):
    print(num)