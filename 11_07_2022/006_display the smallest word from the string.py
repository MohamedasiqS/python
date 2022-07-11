#display the smallest word from the string
str = input ("Enter a sentence\n")
sub_str = str.split()
small = len(sub_str[0])
for i in sub_str:
    if small > len(i):
        sm_str = i
print (sm_str)
