
from math import sin , cos ,tan, factorial, sqrt
#from sympy import*
import math
while True:
    task=input("What do you wany to do? (Simpel math opereration(smo), Trig ,Fact , Sqr ,exit): ")
    if task=="exit":
        break
    elif task=="smo":
        num_1=float(input("Enter a number:"))
        num_2=float(input("Enter a number:"))
        operator= input("Enetr an operator: (+, *, -, /)  or exit:  ")

        if operator=="+":
            result=num_1+num_2
            
        elif operator=="/":
            if num_2!=0:
                result=num_1/num_2
            
            else:
                result="Devied by zero"
        elif operator=="*":
            result=num_1*num_2
            
        elif operator=="-":
            result=num_1-num_2
        print("Results = " ,result)
        
    elif task=="trig":
        angle=int(input("Enter your Angle: "))
        print( "Sin = " ,math.sin(angle))
        print("Cos = ", math.cos(angle))
        print("Cot = " , math.cos(angle)/math.sin(angle))
        print("Tan = " , math.tan(angle))
    elif task=="sqr":
        squre_root=int(input("Enter a number to calculate Squre root : "))
        print("Squer root = ", math.sqrt(squre_root))
    elif task=="Factl":
        num_fact=int(input("Enter a number: "))
        print("Factoreil = ",math.factorial(num_fact))
    


