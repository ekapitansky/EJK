

print(" "), print("\033[5;37;40m Quadratic Equation AX^2 + BX + C\033[0;37;40m\n"), print(" ")

ValidInput=False
while(ValidInput==False):
    try:
        a = float(input('Enter A: '))
        ValidInput=True
    except:
      print("Please enter a number.")

ValidInput=False
while(ValidInput==False):
    try:
        b = float(input('Enter B: '))
        ValidInput=True
    except:
      print("Please enter a number.")

ValidInput=False
while(ValidInput==False):
    try:
        c = float(input('Enter C: '))
        ValidInput=True
    except:
      print("Please enter a number.")

ValidInput=False
while(ValidInput==False):
    try:
        x = float(input('Enter X: '))
        ValidInput=True
    except:
      print("Please enter a number.")

d = (a*x**2)+(b*x)+c
print("Your answer is: ",d)


#print("\033[1;37;40m Quadratic Equation: AX^2 + BX + C\033[0;37;40m \n")
print("\033[5;37;40m Quadratic Equation Solved\033[0;37;40m\n")

print("\033[1;31;40m Quadratic Equation: AX^2 + BX + C \033")
#print("\033[1;37;40m Quadratic Equation: AX^2 + BX + C\033[0;37;40m \n")