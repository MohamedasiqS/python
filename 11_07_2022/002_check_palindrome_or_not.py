#check palindrome or symmetrical or not
print ("Enter String")
str = input()

r_str = str[::-1]

if str == r_str:
    print ("Given string is palindrome")
else:
    print ("Given string is not palindrome")

half = len(str)//2
first_half  = str[:half]
second_half = str[half:]

if first_half == second_half:
    print ("Given string is symmetrical")
else:
    print ("Given string is not symmetrical")

   
    
