#Exp:8 - Program to illustrate Python-MySQL database connectivity.
'''
             Name:- Saqlain Kalokhe
             RollNo:- 20CO22
             Academic Year :- 2021-22
Theory about MySQL and MySQL-Connector-Python:

Python MySQL Connector is a Python driver that helps to integrate Python and MySQL. This Python MySQL library allows the conversion between 
Python and MySQL data types. MySQL Connector API is implemented using pure Python and does not require any third-party library. 

'''
import mysql.connector 

def insert(myc,r,n,a,m,p):
    query="insert into Student values('"+r+"','"+n+"','"+m+"','"+a+"',"+str(p)+")"
    print(query)
    try:
        myc.execute(query)
        myc.execute('commit')
        print('Record inserted successfully..')
    except Exception as e:
        print('Insertion failed..'+str(e))
    
def display(mycursor):
    query='select * from Student'
    mycursor.execute(query)
    for row in mycursor:
        print(row)
    
def update(myc,r,c,v):
    query="update Student set "+c+" = '"+v+"' where Roll_no = '"+r+"'"
    print(query)
    try:
        myc.execute(query)
        myc.execute('commit')
        print('Record Updated successfully..')
    except Exception as e:
        print('Insertion failed..'+str(e))


def delete(myc,r):
    query="delete from Student where Roll_no = '"+r+"'"
    print(query)
    count1=number_of_records(myc)
    myc.execute(query)
    myc.execute('commit')
    count2=number_of_records(myc)
    if (count1>count2):
         print('Record Deleted successfully..')
    else:
        print("The Data for this Roll_no does not exist in the database")     


def number_of_records(myc):
    query='select count(*) from Student'
    myc.execute(query)
    for row in myc:
        count = row[0]
    return count    


def main():
    mydb = mysql.connector.connect(host="localhost",user="danish1",passwd="123")
    mycursor=mydb.cursor()
    mycursor.execute('use Stdmgmt')
    while True:
        print('\t\t\tMENU\n1. Insert.\n2. Display.\n3. Update.')
        print('4. Delete. \n5. Exit.')
        ch=int(input('Enter your choice:: '))
        if ch==5:
            break
        elif ch==1:
            r=input('Enter the Roll No: ')
            n=input('Enter The Name: ')
            m=input('Enter Mobile No: ')
            a=input('Enter The Address: ')
            p=float(input('Enter The Pointer: '))
            insert(mycursor,r,n,a,m,p)
        elif ch==2:
            display(mycursor)

        elif ch==3:
            r=input('Enter the Roll No: ')
            while True:
                print('\t\t\tWhich value do you want to update? \n1. Name.\n2. Mobile No.\n3. Address.\n4. Pointer')
                choice=int(input('Enter your choice'))
                if choice==1:
                    c="Name"
                    v=input('Enter the new value')
                    update(mycursor,r,c,v)
                    break
                elif choice==2:
                    c="Mobile_no"
                    v=input('Enter the new value')
                    update(mycursor,r,c,v)
                    break
                elif choice==3:
                    c="Address"
                    v=input('Enter the new value')
                    update(mycursor,r,c,v)
                    break
                elif choice==4:
                    c="Pointer"
                    v=input('Enter the new value')
                    update(mycursor,r,c,v)
                    break
                else:
                    print("Invalid Choice")

                    

        elif ch==4:
            r=input('Enter the Roll No: ')
            delete(mycursor,r)
        else:
            print('Wrong choice...')

        
if __name__=='__main__':
    main()

#OUTPUT:

'''

                        MENU
1. Insert.
2. Display.
3. Update.
4. Delete.
5. Exit.
Enter your choice:: 1
Enter the Roll No: 20CO40
Enter The Name: Zakki
Enter Mobile No: 7843451197
Enter The Address: Bhiwandi
Enter The Pointer: 9.9
insert into Student values('20CO40','Zakki','7843451197','Bhiwandi',9.9)
Record inserted successfully..
                        MENU
1. Insert.
2. Display.
3. Update.
4. Delete.
5. Exit.
Enter your choice:: 2
('20CO41', 'saqlain', '7506581887', 'Mumbai', 8.9)
('20CO11', 'ayan', '8605482341', 'Seawoods', 9.7)
('20CO07', 'Naved', '7845765483', 'Wadala', 9.7)
('20CO40', 'Zakki', '7843451197', 'Bhiwandi', 9.9)
                        MENU
1. Insert.
2. Display.
3. Update.
4. Delete.
5. Exit.
Enter your choice:: 3
Enter the Roll No: 20CO40
                        Which value do you want to update? 
1. Name.
2. Mobile No.
3. Address.
4. Pointer
Enter your choice4
Enter the new value8.9
update Student set Pointer = '8.9' where Roll_no = '20CO40'
Record Updated successfully..
                        MENU
1. Insert.
2. Display.
3. Update.
4. Delete.
5. Exit.
Enter your choice:: 2
('20CO41', 'saqlain', '7506581887', 'Mumbai', 8.9)
('20CO11', 'ayan', '8605482341', 'Seawoods', 9.7)
('20CO07', 'Naved', '7845765483', 'Wadala', 9.7)
('20CO40', 'Zakki', '7843451197', 'Bhiwandi', 8.9)
                        MENU
1. Insert.
2. Display.
3. Update.
4. Delete.
5. Exit.
Enter your choice:: 4
Enter the Roll No: 20CO40
delete from Student where Roll_no = '20CO40'
Record Deleted successfully..
                        MENU
1. Insert.
2. Display.
3. Update.
4. Delete.
5. Exit.
Enter your choice:: 2
('20CO41', 'saqlain', '7506581887', 'Mumbai', 8.9)
('20CO11', 'ayan', '8605482341', 'Seawoods', 9.7)
('20CO07', 'Naved', '7845765483', 'Wadala', 9.7)
'''