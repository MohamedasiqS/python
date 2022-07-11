#remove i’th character from string
str = input("Enter String\n")

i = (int)(input("Enter ith character to remove from given string\n"))

#for loop in range (0,len(str)):
    #if loop == i:
       # del(str[i]) error: string is immutable it does n't support
str = str[:i-1] + str [i:]

print ("Output is",str)
