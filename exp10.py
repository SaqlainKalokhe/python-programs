#Exp:10-Program to illustrate Multithreeading in Pyhton.
'''         
    Name:- Saqlain Kalokhe
    RollNo:- 20CO22
    Academic Year :- 2021-22
    
Python Multithreading:
Multithreading is a threading technique in Python programming to run multiple threads 
concurrently by rapidly switching between threads with a CPU help (called context switching).
Besides, it allows sharing of its data space with the main threads inside a process that share
information and communication with other threads easier than individual processes. 
Multithreading aims to perform multiple tasks simultaneously, which increases performance,
speed and improves the rendering of the application.

Syntax:
    thread.start_new_thread ( function_name, args[, kwargs] )  
To implement the thread module in Python, we need to import a thread module and then define a 
function that performs some action by setting the target with a variable.

Thread Class Methods:
start():	A start() method is used to initiate the activity of a thread. And it calls only once for each thread so that the execution of the thread can begin.
run():	    A run() method is used to define a thread's activity and can be overridden by a class that extends the threads class.
join():	    A join() method is used to block the execution of another code until the thread terminates.
'''

from threading import *
class A(Thread):
 def run(self):
    for i in range(50):
        print('A')
class B(Thread):
 def run(self):
    for i in range(50):
        print('B')
def main():
 a = A()
 b = B()
 #b = Thread(target=B.run, args=(B(),))
 a.start()
 b.start()
 a.join()
 b.join()
 print('Done')
if __name__=='__main__':
 main()
 
'''
Output:
A
A
A
A
B
A
B
B
B
A
A
B
B
B
B
B
A
A
A
A
B
B
B
B
B
B
A
B
B
B
B
B
A
B
A
A
B
A
A
B
A
B
B
B
B
B
A
A
A
A
B
A
B
B
B
B
A
A
A
A
B
B
B
B
B
A
A
A
B
B
A
A
A
B
A
A
A
B
A
B
B
B
A
B
A
A
B
B
A
A
B
A
B
A
A
A
A
A
A
A
Done
CONCLUSION: 
        In this perticular experiment we have sucessfully implemented multithreading methods like
start(),run() and join().
'''