list = [10,20,30,40,50]

print (list)

print ("Adding Element\n")
list.append(60)
list.append(70)
print (list)

print ("Deleting Element\n")
del list[2]
print (list)


print ("Enter which position want to insert data in list\n")
ch = (int)(input())
print ("Enter new data to add that position\n")
data = (int)(input())
list.insert(ch-1,data)
print (list)


print ("Enter which position want to delete data in list\n")
ch = (int)(input())
del list[ch-1]
print (list)
