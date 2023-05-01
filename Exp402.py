'''

Implementing Exception Handling
        Name-Saqlain Kalokhe
        RollNo-20CO22
        Year-2021-2022
    Theory-An exception can be defined as an unusual condition in a program
    resulting in the interruption in the flow of the program.

Whenever an exception occurs, the program stops the execution, and thus the 
further code is not executed. Therefore, an exception is the run-time errors
that are unable to handle to Python script. An exception is a Python object 
that represents an error

Python provides a way to handle the exception so that the code can be executed
without any interruption. If we do not handle the exception, the interpreter 
doesn't execute all the code that exists after the exception.

Python has many built-in exceptions that enable our program to run without 
interruption and give the output. These exceptions are given below:

The try-expect statement

If the Python program contains suspicious code that may throw the exception, 
we must place that code in the try block. The try block must be followed with 
the except statement, which contains a block of code that will be executed if
there is some exception in the try block.
'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

#driver code
def main():
    while 1:
        try:
            n=int(input("Enter a number"))
            break
        except Exception:
            print("Please enter a valid number")
        else:
            pass
        finally:
            pass
    print(f"The factorial of {n} is {fact(n)}")
if __name__=="__main__":
    main()

'''
Conclusion:In this experiment we implemented exception handling.In this experiment I  understood that
when the exception is handled,the code flow continues without program interruption


Output:     Enter a number6
        The factorial of 6 is 720


'''