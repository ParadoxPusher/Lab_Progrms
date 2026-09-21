def remove_last(lst):
    if lst:
        lst.pop()
    print("Inside function after pop:", lst)

my_list = list(map(int, input("Enter numbers: ").split()))
print("Before function call:", my_list)
remove_last(my_list)

print("After function call:", my_list)