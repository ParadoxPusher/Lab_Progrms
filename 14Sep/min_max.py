int_list = []
for i in range(7):
  # Assign the input to the variable 'num'
  num = int(input("enter the number in the list: "))
  int_list.append(num)

smallest = int_list[0]
for i in range(len(int_list)):
  if int_list[i] < smallest:
    smallest = int_list[i]

print("Smallest number in the list: ", smallest)

largest = int_list[0]
for i in range(len(int_list)):
  if int_list[i] > largest:
    largest = int_list[i]

print("Largest number in the list: ", largest)
