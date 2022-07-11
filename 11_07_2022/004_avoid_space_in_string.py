#count data except space
str = input("Enter string\n")
count = 0
for i in str:
    if i != ' ':
        str = str[:count-1]+str[count:]
        count = count + 1
print(count,str)
"""
    if i not in str.isspace():
        count = count + 1
print(count)
"""
