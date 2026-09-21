def change_string(s):
    s = "X" + s[1:]
    print("Inside function after reassignment:", s)

my_string = input("Enter a string: ")
print("Before function call:", my_string)
change_string(my_string)
print("After function call:", my_string)