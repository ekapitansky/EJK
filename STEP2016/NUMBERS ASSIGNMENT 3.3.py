'''
Overview

Given a set of numbers, create a program that returns the largest and smallest number in the set.

Do not use any existing python functions!

Write a small python program that does the following:
Accepts X amount of numbers from a user
Store each value in a list
Create one or more functions which return the maximum number in the list.
Create one or  more functions which return the smallest number in the list.

Upload your code to GitHub


def numList():
    numList=[]

exit=False
while(exit==False):
    numList=(input('Start tossing me some numbers: '))
    decision=input("Press q to quit.")
    if decision=="q" or decision=="Q":
        exit=True

ValidInput=False
while(ValidInput==False):
    try:
        a = float(input('Enter a number: '))
        ValidInput=True
    except:
      print("Please enter a number.")
'''

a=int(input("How many numbers will you be inputting? "))

numlist=[]

for i in range(0,a):
    numlist.append(int("Start supplying numbers: "))

print(numlist)

















