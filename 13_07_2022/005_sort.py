#sort ascending
ascend = [145,78,23,44,100,58,1]
ascend.sort()
#ascend.sort(reverse = False)
print(ascend)

#sort descending
descend = [145,78,23,44,100,58,1]
descend.sort(reverse = True)
print (descend)

#sort names case insensitive
names = ["Prasanth","kumar","suresh","Balu","Veera"]
names.sort(key = str.lower)
print(names)
