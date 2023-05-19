
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
        angle=float(input("Enter your Angle: "))
        trig_operation=input("Enter what do you want know about this angle (sin,cos,tan,cotg): ")
        if trig_operation=="sin":
            print( "Sin = " ,math.sin(angle))
        elif trig_operation=="cos":
            print("Cos = ", math.cos(angle))
        elif trig_operation=="cotg" or "cot":
            print("Cotg = " , math.cos(angle)/math.sin(angle))
        elif trig_operation==tan:
            print("Tan = " , math.tan(angle))
    elif task=="sqr":
        squre_root=int(input("Enter a number to calculate Squre root : "))
        print("Squer root = ", math.sqrt(squre_root))
    elif task=="Fact" Or "Factoriel" Or "fact" Or "factoriel":
        num_fact=int(input("Enter a number: "))
        print("Factoreil = ",math.factorial(num_fact))
    


