swap = [10,20,30,40,50]

print (swap)

print ("Enter Two position to swap elements")
a = (int)(input())
b = (int)(input())

swap[a-1],swap[b-1] = swap[b-1],swap[a-1]

print (swap)

