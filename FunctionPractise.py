#PART ONE 
def max(a,b):
    if a<b:
        return b
    else:
        return a    
    

#Test Cases:
print('max() results below:')
print(max(2,10))
print(max(4,4)) 
print(max(33,32))
print(max(-50,-5))
print(max(-1,0))   

#Part 2
#1)create your own function called findMax
#2)findMax will take a list as an input
#3)use the max function from Part One to find the maximumm value in the list 
#4)return the maximum value
#hint:create an empty function first and
#hint:test that you can properly call the fn in part 3





def findMax(aList):
    maximum=aList[0]
    bg=0
    for each in aList:
        if each>bg:
            bg=each
    return bg
def sfindMax(aList):
    maximum=aList[0]
    bg=""
    for each in aList:
        if each>bg:
            bg=each
    return bg
list1=[2,6,-4,1]
print(findMax(list1))

#Part 3
#1)Run your findMax fn using the test Cases below as the input
#Test Cases
list1= [4,2,99,32,50]
print('')
list2=['mars','mark','marge','marvel','mares']
list3=['Narwal','Chinese Water Deer','Pangolin','Bat-eared Fox','Markhor']
list4=['Daisy','iris','violet','poppy','lily']

#Example
#We created two fn below called firstFunction() and anotherFunction()
#anotherFunction() uses firstFunction() anfd fwe print the result
#u acn uncomment and run 
#def firstFunction(a,b):
   # return[a,b]
#def anotherFunction(someList):
   # return(firstFunction(someList[1],someList[3]))
#print('anotherFunction() results below: ')
#aList=[1,2,3,4]
#3333333b=anotherFunction(aList)
#print (b)


print("Max value = ", findMax(list1))
print("Max value = ", sfindMax(list2))
print("Max value = ", sfindMax(list3))
print("Max value = ", sfindMax(list4))

import random 
print("Rock , Paper , Scissors")
print("r : Rock")
print("p : Paper")
print("s : Scissors")
user=input("Enter your choice : ")

comp="r"

if user =="r":
    print ("tie")
elif user=="s":
    print ("computer wins")
else:
    print ("user wins")
    



#Your code

   