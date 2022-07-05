num = [1,2,3,4,5,6,7,8,9,10]
odd = []
even = []
for i in num:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print ("Odd List")
print (odd)

print ("Even List")
print (even)
