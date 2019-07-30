#BEGINNING OF CALCULATOR


# 1) use if-statements to complete this calculator program with 4 operations
# Example run (what it should look like):
#       0 - add
#       1 - subract
#       2 - multiply
#       3 - divide
#   Enter a number to choose an operation:
#   1
#   Enter your first input: 10
#   Enter your second input: 4
#   10 - 4 = 6

# 2) add a fifth operation, power, that does a to the power of b
# 3) add a sixth operation, square root, that only asks for 1 input number and outputs its sqrt
# 4) seventh operation, factorial(a), one input
# 5) eighth operation, fibonacci(a), one input
# 6) talk to instructors when finished

import math
print("                CALCULATOR  ")
print("                 0 - add")
print("                 1 - subract")
print("                 2 - multiply")
print("                 3 - divide")
print("                 4 - power")
print("                 5 - square root")
print("                 6 - factorial")
print("                 7 - fibonacci")
ans="yes"



while ans=="yes" :
    op = int(input("                Enter a number to choose an operation:"))
    if op==7:
        nterm=int(input("           Input the number of terms:"))
        n1=0
        n2=1
        count=0
        while(count<nterm):
            print(n1,",")
            nth=n1+n2
            n1=n2
            n2=nth
            count=count+1
    else:        

        a = int(input("                 Enter the number: "))
        if op==5 or op==6:
            if op==5:
                print(math.sqrt(a))
            else:
                print(math.factorial(a))
        elif op<5:
            b = int(input("         Enter your second input: "))  
            if op == 0:
                print(a+b)
            elif op == 1:
                print(a-b)
            elif(op==2):
                print(a*b)    
            elif(op==3):
                if(a>b):
                    print(a/b)
                else:
                    print(b/a)     
            elif(op==4):
                print(a**b)
            else:
                 print("            Invalid loop")  
    ans=input("                      Do you want to use it again ? ")             
#END OF CALCULATOR          
         






       


    









        
    








 




