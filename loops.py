# Listing all the even Numbers under 100
Numbers = 100
while Numbers > 0:
    print(Numbers)
    Numbers -= 2

#Multiplication table
Number=int(input("Please eneter a number :"))
print("Multiplication of", Number)
for i in range(1,11):
    print(Number, "x", i, "=", (Number * i))

    Mynames=[]
    counter=1
    while counter != 0:
        strName=input("Please enter name")
        Mynames.append(strName)
        coounter=1
    print('Mynames')