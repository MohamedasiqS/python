#abcdefgh  O/P : ab2cd4ef6gh8
strr = input("Enter string\n")
two = 2
inc = 2
for i in range(0,len(strr),two):
    strr = strr[:i+2]+str(inc)+strr[i+3:]
    inc =inc + 2
print (strr)
