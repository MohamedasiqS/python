#change list items

fruit = ["Apple","Banana","Grapes","Guava","Jackfruit"]
print (fruit)
#First Way
fruit[2] = "Strawberry"
print (fruit)
#Second Way
fruit[2:3] = ["Grapes"]
print (fruit)

#append

num = ["one","two","three","four"]
print ("Before Append")
print (num)
num.append("five")
print ("After Append")
print (num)

#insert
name = ["rahul","rajesh","santhosh","dinesh"]
print (name)
name.insert(2,"ravi sasthri")
print (name)

#extend
list1 = ["one","two","three","four"]
list2 = ["apple","ball","cat","dog"]
list1.extend(list2)
print (list1)

#remove
name = ["rahul","rajesh","santhosh","dinesh","suresh"]
name.remove("rajesh")
print (name)
