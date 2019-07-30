import random
a=[]
for i in range(10):
    a.append(random.randint(0,100))
s=0
for x in a:
    print(x)
    s=s+x
print(s)
#MULTIPLICATION TABLE
#n=int(input("Input a number : "))
#for i in range(1,11):
#    print(n,"x",i,"=",n*i)
#--------------------------

print("This is a programme to print all the print numbers till : ")
n=int(input("Input the number till which you wanna check : "))

for i in range(2,n):
 
       for k in range(2,i):
           if (i % k) == 0:
               break
       else:
           print(i) 
                      
           
           


