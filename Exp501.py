#Exp:5 : Menu driven program for data structure using built in function for link list, stack and queue.

'''
             Name:- Saqlain Kalokhe
             RollNo:- 20CO22
             Academic Year :- 2021-22
THEORY :

 STACK
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one
end and an element is removed from that end only. The insert and delete operations are often called push and pop.
Implementation using list: Pythons built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of the stack 
                           while pop() removes the element in LIFO order. 

QUEUE
Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. 
A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.
Implementation using collections.deque : Queue in Python can be implemented using deque class from the collections module. Deque is preferred over list in the 
                                         cases where we need quicker append and pop operations from both the ends of container

LINKED LIST
A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of 
a pointer. Python does not have linked lists in its standard library. We implement the concept of linked lists using the concept of nodes
Implementation of linked lists : A linked list is created by using the node class. We create a Node object and create another class to use this ode object. We pass 
                                 the appropriate values through the node object to point the to the next data elements.


'''

from collections import deque

class Stack:
    def __init__(self):
        self.data=list()
    def push(self,d):
        try:
            self.data.append(d)
        except Exception:
            return False
        return True
    def pops(self):
        if not self.data:
            return "Stack is empty"
        return "Popped element is:-"+str(self.data.pop())
    
    def display(self):
        if not self.data:
            print('Stack is empty.')
        else:
            print('Stack Content ->',self.data[::-1])
    
    def __str__(self):
        if not self.data:
            return 'Stack is empty.'
        else:
            return 'Stack Content -> '+str(self.data[::-1])

class Queue:
    def __init__(self):
        self.data = deque()
        
    def insert(self,d):
        self.data.append(d)
        
    def remove(self):
        if self.data:
            return "Removed Element is "+str(self.data.popleft())
        else:
            return "Cant remove from an empty Queue."
        
    def display(self):
        if not self.data:
            print('Queue is empty.')
        else:
            print('Queue Content ->',end=" ")
            for i in self.data:
                print(i,end="\t")
            print()

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self,data=None):
        if data:
            self.head = Node(data)
        else:
            self.head = None
            
    def insertAtBeg(self,d):
        newnode = Node(d)
        newnode.next = self.head
        self.head = newnode
        return "Node Inserted"
        
    #Implement below functions
    def insertAtEnd(self,d):
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(d)
            return "Node Inserted."
        else:
            self.head=Node(d)
            return "Node Inserted"
            
    def removeFirst(self):
        if self.head is None:
            return "Cannot remove list is empty."
        if self.head.next:
            temp=self.head
            self.head=temp.next
            return "Node Removed."
        else:
            self.head=None
            return "Node Removed."
            
    def removeLast(self):
        if self.head is None:
            return "Cannot remove list is empty."
        
        if self.head.next:
            temp=self.head
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            return "Node Removed."
        else:
            self.head=None
            return "Node Removed."
    
    
    def insertAfter(self,key,d):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
            if temp:
                newnode = Node(d)
                newnode.next = temp.next
                temp.next = newnode
                return "Node inserted."
            return "Key Node does not exist."
        
    def removeBefore(self,key):
        temp = self.head
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
            if temp == self.head:
                return "Cannot remove before first node."
            elif temp:
                if prev == self.head:
                    self.head = prev.next
                else:
                    temp = self.head
                    while temp.next != prev:
                        temp = temp.next
                    temp.next = prev.next
                    prev.next = None
                return "Node Removed."
            return "Key Node does not exist."
    
    def display(self):
        if self.head:
            temp = self.head
            print('Linked List:')
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            print('Linked List is empty.')


# modify main function to have MENU with all required options    
def main():
    s1=Stack()
    while 1:
        print("\t\tMENU\n")
        try:
            ch=int(input("1.Stack\n2.Queue\n3.Linked List\n4.Exit Program "))
        except Exception:
            print("Invalid Input")
        else:
            if ch==1:
                stack()
            elif ch==2:
                queue()
            elif ch==3:
                linked()
            elif ch==4:
                break
            else:
                print("Invalid Input")
                    
                    
def stack():
    s1=Stack()
    while 1:
        print("\t\tMENU(STACK)\n")
        try:
            ch=int(input("1.Push Data\n2.Pop Data\n3.Display\n4.Exit To Main Menu"))
        except Exception:
            print("Invalid Input")
        else:
            if ch==1:
                data=int(input("Enter the data"))
                s1.push(data)
            elif ch==2:
                print("\n",s1.pops())
                            
            elif ch==3:
                s1.display()
            elif ch==4:
                break
            else:
                print("Invalid Input")

def queue():
    q1=Queue()
    while 1:
        print("\t\tMENU(QUEUE)\n")
        try:
            ch=int(input("1.Insert\n2.Pop Data\n3.Display\n4.Exit To Main Menu "))
        except Exception:
            print("Invalid Input")
        else:
            if ch==1:
                data=int(input("Enter the data"))
                q1.insert(data)
            elif ch==2:
                print("\n",q1.remove())
            elif ch==3:
                q1.display()
            elif ch==4:
                break
            else:
                print("Invalid Input")
        
def linked():
    l1=Linked_List()
    while 1:
        print("\t\tMENU(LINKED LIST)\n")
        try:
            ch=int(input("1.Insert at Beg\n2.Insert at Last\n3.Remove First\n4.Remove Last\n5.Insert After\n6.Remove Before\n7.Display\n8.Exit to Main Menu "))
                        
        except Exception:
            print("Invalid Input")
        else:
            if ch==1:
                data=int(input("Enter the data"))
                print("\n",l1.insertAtBeg(data))
            elif ch==2:
                data=int(input("Enter the data"))
                print("\n",l1.insertAtEnd(data))
            elif ch==3:
                print("\n",l1.removeFirst())
            elif ch==4:
                print("\n",l1.removeLast())
            elif ch==5:
                key=input("Enter the data after which you want to insert")
                data=int(input("Enter the data "))
                print("\n",l1.insertAfter(key,data))
            elif ch==6:
                key=input("Enter the data before which you want to remove")
                print("\n",l1.removeBefore(key))
            elif ch==7:
                l1.display()
            elif ch==8:
                break
            else:
                print("Invalid Input")
                      
if __name__=='__main__':
    main()

'''
Output:
                MENU

1.Stack        
2.Queue        
3.Linked List  
4.Exit Program 1
                MENU(STACK)

1.Push Data
2.Pop Data
3.Display
4.Exit To Main Menu1       
Enter the data34
                MENU(STACK)

1.Push Data
2.Pop Data
3.Display
4.Exit To Main Menu3       
Stack Content -> [34]      
                MENU(STACK)

1.Push Data
2.Pop Data
3.Display
4.Exit To Main Menu2

 Popped element is:-34
                MENU(STACK)

1.Push Data
2.Pop Data
3.Display
4.Exit To Main Menu3
Stack is empty.
                MENU(STACK)

1.Push Data
2.Pop Data
3.Display
4.Exit To Main Menu4
                MENU

1.Stack
2.Queue
3.Linked List
4.Exit Program 2
                MENU(QUEUE)

1.Insert
2.Pop Data
3.Display
4.Exit To Main Menu 1
Enter the data24
                MENU(QUEUE)

1.Insert
2.Pop Data
3.Display
4.Exit To Main Menu 3
Queue Content -> 24
                MENU(QUEUE)

1.Insert
2.Pop Data
3.Display
4.Exit To Main Menu 2

 Removed Element is 24
                MENU(QUEUE)

1.Insert
2.Pop Data
3.Display
4.Exit To Main Menu 3
Queue is empty.
                MENU(QUEUE)

1.Insert
2.Pop Data
3.Display
4.Exit To Main Menu 4
                MENU

1.Stack
2.Queue
3.Linked List
4.Exit Program 3
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 7
Linked List:
24
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 1
Enter the data14

 Node Inserted
                 MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 2
Enter the data34

 Node Inserted.
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 7
Linked List:
14
24
34
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 5
Enter the data after which you want to insert24
Enter the data 44

 Node inserted.
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 7
Linked List:
14
24
44
34
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 6
Enter the data before which you want to remove24

 Node Removed.
                MENU(LINKED LIST)

1.Insert at Beg
2.Insert at Last
3.Remove First
4.Remove Last
5.Insert After
6.Remove Before
7.Display
8.Exit to Main Menu 7
Linked List:
24
44
34

'''