def countdown(n):
    while n > 0:
        yield n
        n -= 1


n=int(input("Enter the Number to Start the countdown from: "))
print("Countdown:")
for number in countdown(n):
    print(number)