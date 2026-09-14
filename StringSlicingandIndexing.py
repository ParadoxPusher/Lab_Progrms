word = input("Enter the string: ")
print(word[:3])
print(word[-2::])

for i in range(len(word)):
  if i % 2 != 0:
    print(word[i], end="") 

print(word[::-1])
