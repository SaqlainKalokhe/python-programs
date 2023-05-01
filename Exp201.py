'''
For Loop in python

    Name:Saqlain Kalokhe
    Roll No:20CO22
    2021-22
    
   THEORY:
   
    For Loop:- A for statement includes the following:
                The for keyword
                A variable name
                The in keyword
                A call to the range() method with up to three integers passed to it
                A colon
                Starting on the next line, an indented block of code(called the for clause)
                
    range() function of for loop:- The range() is a built-in function in Python. Syntax of range() function is:
                                       range([start,] stop[,step])
                                    All the parameters of range() function must be integers. The step parameter can be postive
                                    or a negative integer exculding zero.
'''


num=int(input('Enter a number: '))
fact=1
for i in range(1,num+1):
    fact=fact*i
print('Factorial of',num,'is',fact)

for row in range(1,6):
    for col in range(1,6):
        if row<=col:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print()  
s='*'*3 + '\n' +'*'*2 + '\n' + '*'
print(s)

'''
OUTPUT:
    Enter a number: 5
    Factorial of 5 is 120
    *****
     ****
      ***
       **
        *

    ***
     **
      *
'''

'''
Conclusion: So in this program we found the factorial of number taken from the user and formed 
            2 patterns using the for loop.
            In this perticular experiment we have sucessfully implemented for loop. for loop
            provides code re-usability. 
            Using loops, we do not need to write the same code again and again.
            Using loops, we can traverse over the elements of data structures (array or linked lists).
            
'''