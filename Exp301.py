'''
  IMPLEMENTING CLASSES AND OBJECTS IN PYTHON
      @author
    Name:Saqlain Kalokhe
    Roll No:20CO22
    2021-22   
    THEORY: A class is a virtual entity and can be seen as a blueprint of an object. 
        The class came into existence when it instantiated.
        
        Let's understand it by an example.
Suppose a class is a prototype of a building. A building contains all the details about the floor,
rooms, doors, windows, etc. we can make as many buildings as we want, based on these details.
Hence, the building can be seen as a class, and we can create as many objects of this class.

On the other hand, the object is the instance of a class. The process of creating an object can be 
called instantiation.

Creating classes in Python
In Python, a class can be created by using the keyword class, followed by the class name.
    
    docstring -> documentation string
'''

from lib2to3.pgen2.token import AMPER
from re import L
from unicodedata import name


class Employee:
    '''
    An Employee class having employee attributes like empno, ename and sal.
    It also has methods like setprop, display, etc.
    '''
    empno=None
    ename=None
    sal=None
    dept=None
    loc=None
    def setprop(self,num,name,sal,dept,loc):
        self.empno=num
        self.ename=name
        self.sal=sal
        self.dept=dept
        self.loc=loc
    def getprop(self):
        return self.empno,self.ename,self.sal,self.dept,self.loc
    
    # In Python, static methods are simply used as utility functions
    @staticmethod        # decorator
    def retire(age):
        if age>=60:
           print("Employee retires")
        else:
            print("Employee can still work")
        

# driver code
def main():
    '''
    Our main function of Exp301 having a driver code.
    '''
    e=Employee()
    e.setprop(1,"Sachin",30000,"Computer","Mumbai")
    en,name,sal,dept,l=e.getprop()
    print(en,name,sal,dept,l)
    e1=Employee()
    e1.setprop(2,"shamim",40000,"Computer","Navi Mumbai")
    e2=Employee()
    e2.setprop(3,"Khatib",50000,"Computer Testing","Navi Mumbai")
    
    if e.sal > e1.sal:
        print(e.getprop())
    else:
        print(e1.getprop()) 
        
    el=[e,e1,e2]
    sal=0
    emp_hs=Employee()
    for i in el:
        if i.sal>sal:
            sal==i.sal
            emp_hs=i
            
    print("Employee with highest salary is",emp_hs.ename)
    Employee.retire(42) 
    #print(e1[0].ename)
    
   

if __name__=="__main__":
    print(main.__doc__)
    main()

'''
OUTPUT:

    Our main function of Exp301 having a driver code.
    
1 Sachin 30000 Computer Mumbai
(2, 'shamim', 40000, 'Computer', 'Navi Mumbai')
Employee with highest salary is Khatib
Employee can still work

'''

'''
CONCLUSION: In this experiment we have successfully implemented class and its objects
            I understood that class is used for defining a particular type of object. Because
            Python objects can have both function and data elements
'''