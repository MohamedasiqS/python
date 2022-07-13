#Loop
list = ["one","two","three","four"]
for i in list:
    print (i)

#Loop through index number
list = ["one","two","three","four"]
i = 0
while i < len(list):
    print (list[i])
    i = i + 1

#List Comprehension
list = ["one","two","three","four"]
[print(i) for i in list]
