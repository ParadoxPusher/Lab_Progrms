raw_input = input("Enter integers separated by space: ")
numbers = [int(x) for x in raw_input.split()]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"Original list: {numbers}")
print(f"List without duplicates: {unique_numbers}")
