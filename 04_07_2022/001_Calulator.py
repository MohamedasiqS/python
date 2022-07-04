a = int(input ("Enter A value\n"))
b = int (input ("Enter B value\n"))

print ("Enter choice\n1.Add\n2.Sub\n3.Multiply\n4.Divide")

choice = (int)(input())

if (choice == 1):
    print (a+b)

elif (choice == 2):
    print (a-b)

elif (choice == 3):
    print (a*b)

elif (choice == 4):
    print (a/b)

else :
    print ("Invalid option")
