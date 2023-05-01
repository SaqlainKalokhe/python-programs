'''
Inheritance
Diamond Problem (Ambiguity Problem)

                A
            B       C
                D
'''


class Person:
    name=None
    addr=None
    age=None
    contact=None
    def _init_(self,n=None,a=None,age=None,c=None):
        self.name=n
        self.addr=a
        self.age=age
        self.contact=c
        print('I m in Person Class.',Person._base_)
    def setprop(self,n,a,age,c):
        self.name=n
        self.addr=a
        self.age=age
        self.contact=c
    def getprop(self):
        return self.name,self.addr,self.age,self.contact

class Employee(Person):
    empno=None
    dept=None
    loc=None
    def setemp(self,e,n,a,age,c,d,l):
        self.empno=e
        self.dept=d
        self.loc=l
        self.setprop(n,a,age,c)
    def getemp(self):
        #return self.empno,self.name,self.age,self.dept,self.loc
        return self.empno,self.getprop(),self.dept

class Student(Person):
    rollno=None
    classroom=None      #FECO or SECO or TECO or BECO
    ptr=None
    def setstud(self,r,n,a,age,c,cr,p):
        self.rollno=r
        self.classroom=cr
        self.ptr=p
        self.setprop(n,a,age,c)
    def getstud(self):
        return self.rollno,self.getprop(),self.classroom,self.ptr



#driver code
def main():
    e=Employee()
    e.setemp(1,"Ahmed Khan","Mumbai",28,9898998989,"Cyber Security","Pune")
     
    print(e.getemp())
    s=Student()
    s.setstud("20CO01","Ahmed Shaikh","Navi Mumbai",18,9899998999,"SECO",8.9)
    print(s.getstud())

if __name__=="__main__":
    main()
    
    
'''
OUTPUT: 

(1, ('Ahmed Khan', 'Mumbai', 28, 9898998989), 'Cyber Security')
('20CO01', ('Ahmed Shaikh', 'Navi Mumbai', 18, 9899998999), 'SECO', 8.9)

'''
'''
CONCLUSION:
'''