# First program of SBLC lab
'''
   BASIC CONCEPTS OF PYTHON
               
               Name:Saqlain Kalokhe
               RollNO:20CO22
               2021-22
               
Theory about the program: 

  A] Comments in python: Commenting in Python is very helpful for programmers, but they are not considered by the interpreter.
                   Single-line comments: In Python, we use the hash symbol # to write a single-line comment.
                                        E.g. #this is a single-line comment.
                                        
                   Multi-line comments: Although Python doesn't support a separate method for writing multiline comments, 
                                        there are ways to get around it.
                                        
                                1.Using multiple # :  E.g #this is            #a multiline        #comment.
                                
                                2.Using String Literals to write Multi-line Comments :  Using triple quotes, 
                                 Here the multiline string isn't assigned to any variable,         
                                 so it is ignored by the interpreter. Even though it is not technically a multiline comment, 
                                 it can be used as one. 
                                 E.g. this documentation is written using multiline comments.  
                                 
  B] Datatypes in python :In Python, each value has a datatype. Data types are essentially classes, and variables are 
                          instances (objects) of these classes, because everything in Python programming is an object. 

                NUMBERS IN PYTHON :Python numbers include integers, floating point numbers, and complex numbers. 
                                   In Python, they are known as int, float, and complex classes. 

                STRINGS IN PYTHON :The term "string" refers to a collection of Unicode characters. To represent strings, 
                                   we can use single or double quotations. 
                                   Triple quotes can be used to represent multi-line strings. 

 C] Python Expressions : Expressions are value representations. They differ from statements in that statements perform a 
                         function, whereas expressions convey a value. Any string, for example, is an expression because 
                         it also represents the string's value. 
                         
 D] Input and Output functions :
                        Python output using print() function :To output data to the standard output device, we use the print() 
                                                              method (screen). Data can also be saved to a file. 
                                                              For instance, print ("Hello world") 
                                                              
                        Python input using the input() function: We may want to take user input to provide for more flexibility. 
                                                                The input() method in Python allows us to do this. 
                                                                 As an example, input ("Enter a number:")

     
'''
i=10
print("Data =",i,"and its type is",type(i),"and its location is",id(i))
#print(id(i))
f=20.5
print("data =",f,"and its type is",type(f),"and its location is",id(f))
s="aiktc"
print("data =",s,"and its type is",type(s),"and its location is",id(s))

#var=float(input("Enter the data: "))
#print("Scanned data is ",var,"and its type is ",type(var))

#Indentation: Used to specify a blog

var1=int(input("Enter the data: "))
var2=int(input("Enter the data: "))
var3=int(input("Enter the data: "))
if var1>var2>var3:
        print("first number is greater")
elif var2>var3:
        print("second number is greater")
elif var1==var2==var3:
        print("All number are equal ")
else:
        print("Third number is greatest")

'''OUTPUT:
('Data =', 10, 'and its type is', <type 'int'>, 'and its location is', 5721067424)
('data =', 20.5, 'and its type is', <type 'float'>, 'and its location is', 5721075424)
('data =', 'aiktc', 'and its type is', <type 'str'>, 'and its location is', 4382692096)
Enter the data: 10
Enter the data: 20
Enter the data: 30
Third number is greatest
'''
''' 
CONCLUSION: Comments are description to understand the functionality of program.
            Every datatype is a class in python.
            Expressions are representation of values.
            Input() function is used to take input from user.
            Print() function is used to display output to the user. 
'''
    
