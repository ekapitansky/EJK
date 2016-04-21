'''
def ftemp():



    ftemp=float(input("Enter the temperature: "))
    ctemp=(ftemp-32)/1.8
    print("The temperature is ",ctemp)

ftemp()



mystring="apple"
count=len(mystring)
print(count)

for a in range (0,count):
    print(mystring[a])

c=0
while c<count:
    print(mystring[c], end=" ")
    c+=1


mystring="apple         "
mystring=mystring.strip()
mystring=mystring.upper()
print(mystring)
'''

for celsius in range (0,101,5):
    print("Celsius: ",celsius, "Fahrenheit: ",(1.8*celsius+32))


# ctemp=(ftemp-32)/1.8