str_in = input("Enter words: ")
words = str_in.split()
frequency = {}

for i in words:
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1

word = list(frequency.keys())
value = list(frequency.values())

for i in range(len(word)):
  print(word[i], ":", value[i])
