
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
         print(namelist[a], colorlist[a])

main()
