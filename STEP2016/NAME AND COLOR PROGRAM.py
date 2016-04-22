
'''
def main():
    listprogram()

def listprogram():
    namelist=[]
    colorlist=[]
    exit=False
    while(exit==False):
        namelist.append(input("What is your name? "))
        colorlist.append(input("What is your favorite color? "))
        decision=input("Press q to quit. ")
        if decision=="q" or decision=="Q":
            exit=True
    length=len(namelist)
    for a in range(0,length ):
         print( namelist[a], colorlist[a])


main()

'''
'''


print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
'''

def main():
    listprogram()

def listprogram():
    newlist=[] # Will contain all names and colors

    exit=False
    while(exit==False):
        newlist.append(input("What is your name? "))
        newlist.append(input("What is your favorite color? "))
        decision=input("Press q to quit. ")
        if decision=="q" or decision=="Q":
            exit=True
    length=len(newlist)
    for a in range(0,length,2):
         print( newlist[a], end=" ")
         print(newlist[a+1])


main()