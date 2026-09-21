str_in = input("Enter the string: ")
new_str=''
for i in range(len(str_in)):
  ascii_val = ord(str_in[i])
  if ascii_val == 32 or (48 <= ascii_val <= 57) or (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
    new_str+=str_in[i]

print(new_str)
