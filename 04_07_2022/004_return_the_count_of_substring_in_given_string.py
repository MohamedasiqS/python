def count_substring (str,s_str):
    count = 0
    for i in range(len(str)):
         if str[i:i+len(r_str)] == r_str :
             count = count + 1
    print (count)
    return count

print ("Enter sentence")
str = input()
print ("Enter substring to count in given sentence")
r_str = input()

ret = count_substring (str,r_str)

print ("sub-string occured",end=' ')
print (ret,end=' ')
print ("times")
