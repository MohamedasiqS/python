def is_palindrome(num):
    rem = 0
    quo = num
    p_num = 0
    while quo != 0:
        rem   = quo % 10
        p_num = p_num*10 + rem
        quo   = quo //10
    
    if num == p_num:
        return True
    else:
        return False

print ("Enter Number")
num = (int)(input())
ret = is_palindrome(num)

if ret == 1:
    print ("Given number is paindrome")
else:
    print ("Given number is not palindrome")

"""
101
1

"""
