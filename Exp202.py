'''
  Implementing functions in python
    @author
    Name:Saqlain Kalokhe
    Roll No:20CO22
    2021-22   
                     
    THEORY: Functions are named blocks of code that are designed to done one specific job. A function is like
            a mini-program within a program.
            When you want to perform a particular task that you've defined in a function, you call the name
            of the function responsible for it. If you need to perform that task multiple times throughout
            your program, you don't need to type all the code for the same task again and again; you just call
            the function dedicated to handling the task, and the call tells Python to run the code inside the
            function. You'll find that using functions make your programs easier to write, read, test and fix. 
  
'''

def fact(num):
   f=1
   for i in range(1,num+1):
       f=f*i
   return f

def fibo(num):
    a=0
    b=1
    if num==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            print(c)

def palin(num):
    rev=0
    q=num
    while q>0:
        
        rev=rev*10+q%10
        q=q//10
        
    if num==rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
        

if __name__=='__main__':
     while True:
         print("Menu:\n\t1.Factorial\n\t2.Fibonacci\n\t3.Palindrome")
         ch=int(input("Enter a number:"))
         if ch==1:
             n=int(input("Enter a number:"))
             print(f"The factorial of {n} is {fact(n)}")
         elif ch==2:
             f=int(input("Enter a number:"))
             print(f"The fibonacci series of {f} is ")
             fibo(f)
         elif ch==3:
             n=int(input("Enter a number to find reverse:"))
             palin(n)
         else:
             print("Please enter a correct number")

'''
OUTPUT:    
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
Enter a number:1
Enter a number:6
The factorial of 6 is 720
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
Enter a number:2
Enter a number:5
The fibonacci series of 5 is 
0
1
1
2
3
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
Enter a number:3
Enter a number to find reverse:123
Not a palindrome number
'''

'''
CONCLUSION: Therefore, in this program we found the factorial of a number taken from the user, Fibonacci
            series of a given number and checked whether the number taken from the user is palindrome or not
            using Functions.  
'''