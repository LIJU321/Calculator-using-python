from math import *
import pygame
import sys

def main():
    print("\nhello which operation would do you like to do ?, press the corresponding number ")
    user_response=int(input("for *multipliaction= 1, for /division=2, for addition=3, for substraction=4,for modulus=5 and for power=6:\n\tyour choice?:"))


    if user_response==3:
       addition()
    if user_response==4:
        substraction()
    if user_response==1:
       Multiplication()
    if user_response==2:
        Division()
    if user_response==5:
         Modulus()
    if user_response==6:
         Power()
  
    else:
        print("invalid command")
        main()

def Power(): #power function from math library 
    first_num=[1,2]
    num=int(input("enter the number to give exponent:"))
    num2=int(input("enter the exponent value:"))
    first_num[0]= num
    first_num[1]= num2
    power= pow(first_num[0],first_num[1])
    print("the result =",power)
    main()
    
def Modulus():
    first_num=[1,2]
    num=int(input("enter the dividend:"))
    num2=int(input("enter the second num to divisor:"))
    first_num[0]= num
    first_num[1]= num2
    sumof = first_num[0]%first_num[1]
    print("the reminder is =",sumof)
    main()
    


def Multiplication():
    first_num=[1,2]
    num=int(input("enter the numbers to multiply:"))
    num2=int(input("enter the second num to multiply:"))
    first_num[0]= num
    first_num[1]= num2
    sumof = first_num[0]*first_num[1]
    print(sumof)
    main()
    
def Division():
    first_num=[1,2]
    num=int(input("enter the numbers to division:"))
    num2=int(input("enter the second num to division:"))
    first_num[0]= num
    first_num[1]= num2
    sumof = first_num[0]/first_num[1]
    print(sumof)
    main()
        


def addition():
    first_num=[1,2]
    num=int(input("enter the numbers to add:"))
    num2=int(input("enter the second num to add:"))
    first_num[0]= num
    first_num[1]= num2
    sumof = first_num[0]+first_num[1]
    print(sumof)
    main()
    
def substraction():
    first_num=[1,2]
    num=int(input("enter the numbers to substract:"))
    num2=int(input("enter the second num to substract:"))
    first_num[0]= num
    first_num[1]= num2
    sumof = first_num[0]-first_num[1]
    print(sumof)
    main()
    
main()

















