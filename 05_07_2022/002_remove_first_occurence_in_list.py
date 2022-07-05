list = [10,20,30,40,50,30]
print (list)

for i in range(0,len(list)):
    for j in range (i+1,len(list)):
        if list[i] == list[j]:
            list.remove(list[i])
            break
print (list)

