def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

c = float(input("Enter temperature in Celsius: "))

f = celsius_to_fahrenheit(c)
print(f"Temperature in Fahrenheit: {f:.2f}°F")