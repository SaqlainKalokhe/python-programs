#Exp: 602- Python program to count number of lines, words and characters in a file.
'''
           Name:- Saqlain Kalokhe
           RollNo:- 20CO22
           Academic Year :- 2021-22
           
THEORY: Counting the lines, word, and characters within a text file results in the line count, word count, and character count, which includes spaces. For 
        instance the text file containing "Hello World\nHello Again\nGoodbye" results on lines: 3 words: 5 characters: 29

''' 
def readl(fname):
    no_of_lines = 0
    with open(fname+".txt",'r') as file:
        print("\nThe Number of lines in the text file are:")
        for i in file:
            no_of_lines += 1
        print(no_of_lines)

def readc(fname):
    with open(fname+".txt",'r') as file:
        data=file.read()
        print("\nThe Number of characters in the text file are:")
        print(len(data))


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
            print("1.Number of lines in the File\n2.Number of characters in the File\n3.Exit ")
            ch=int(input("Enter choice "))
            if ch==1:
                readl(fname)
            elif ch==2:
                readc(fname)
            elif ch==3:
                break
            else:
                print("Invalid Input")
                
                
                
if __name__=="__main__":
    main()

'''
Output:
Enter the file name text
                Menu

1.Number of lines in the File     
2.Number of characters in the File
3.Exit 
Enter choice 1

The Number of lines in the text file are:
4
                Menu

1.Number of lines in the File
2.Number of characters in the File
3.Exit
Enter choice 2

The Number of characters in the text file are:
94
                Menu

1.Number of lines in the File
2.Number of characters in the File
3.Exit
Enter choice 3

Conclusion: We have successfully counted number of lines, words and characters in a file.
'''    