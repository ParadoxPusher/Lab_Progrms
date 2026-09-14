int_lst = []
for i in range(10):
  num = int(input("Enter the number: "))
  int_lst.append(num)

sum = 0
average = 0
for i in range(len(int_lst)):
  sum += int_lst[i]

print("sum of the list: ", sum)
print("Average of the list ", sum/len(int_lst))
