#Exp:-601:- Python program to append data to existing file and then display the entire file.
'''
           Name:- Saqlain Kalokhe
           RollNo:- 20CO22
           Academic Year :- 2021-22

File Handling in Python:
Python too supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling 
options, to operate on files. 

Working of open() function
Before performing any operation on the file like read or write, first we have to open that file. For this, we should use Python's 
inbuilt function open().But at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

The following are the modes :
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a:  open an existing file for append operation. It won't override existing data.
r+:  To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won't override existing data.


'''
def write(fname):
    with open(fname+".txt","a+") as file:
        file.seek(0)
        data=file.read()
        if len(data)>0:
            file.write("\n")    
        data=input("Enter the data to write to file ")
        file.write(data)
       
            
def read(fname):
    with open(fname+".txt",'r') as file:
        print("\nThe contents of the text file are:\n")
        for i in file:
            print(i)
        print("\n")
    

def main():
    fname=input("Enter the file name ")
    try:
        with open(fname+".txt",'r') as file:
            pass
    except Exception:
        print("File does not exist")
    else:        
        while 1:
            print("\t\tMenu\n")
            print("1.Write contents of file\n2.Read file content\n3.Exit ")
            ch=int(input("Enter choice "))
            if ch==1:
                write(fname)
            elif ch==2:
                read(fname)
            elif ch==3:
                break
            else:
                print("Invalid Input")
                
                
                
if __name__=="__main__":
    main()

'''
Output: 
                Menu

1.Write contents of file
2.Read file content
3.Exit
Enter choice 1
Enter the data to write to file Hi, Welcome to python world.
                Menu

1.Write contents of file
2.Read file content
3.Exit
Enter choice 2

The contents of the text file are:

Hi, Welcome to python world.


                Menu

1.Write contents of file
2.Read file content
3.Exit
Enter choice 3

Conclusion: In this experiment, we have successfully appended data to existing file using Append mode(a) and then displaywd the entire file using the Read mode(r).
'''

                
