'''
firstlist=[1,2,3,4,5,5,6]
#print(firstlist[2])
for a in firstlist:
    print(a, end=" ")


def main():
    iterations= getIterations()
    x(iterations)

def getIterations():
    return int(input("How many names will you add?"))

def getColors():

    def x(y):
        firstlist=[]
        a=0
    for a in range(0,y):
        names=int(input("Enter your name: "))
        firstlist.append(names)

main()
'''


def listprogram():
    namelist=[]
    colorlist=[]
    exit=False
    while(exit==False):
        namelist.append(input("What is your name?"))
        colorlist.append(input("What is your favorite color?"))
        decision=input("Press q to quit.")
        if decision=="q" or decision=="Q":
            exit=True
    length=len(namelist)
    for a in range(0,length ):
         print(namelist[a]. colorlist[a])

