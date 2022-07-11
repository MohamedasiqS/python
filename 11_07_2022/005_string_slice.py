"""
abcdefgh
ab2cd4ef6gh8
"""

str = "abcdefgh"
a=0
for i in range(1,len(str),2):
    a = a+2
    str = str[:i+2]+format(a)+str[i+2:]
print (str)
