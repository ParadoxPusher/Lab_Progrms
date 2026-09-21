word = input("Enter the string: ")
print(word.upper())
print(word.lower())
print(word[::-1])

count = 0
for i in word:
  if i in 'aeiou':
    count = count + 1
    
print("Number of vowels: ", count)
