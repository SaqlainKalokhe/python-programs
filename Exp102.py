'''
   Implementing data types like List, Set, Tuple and Dictionary
    @author
    Name:Saqlain Kalokhe
    Roll No:20CO22
    2021-22

   THEORY :

   a)List:-A list can be defined as a collection of values or items of different
           types. The items in the list are separated with the comma (,) and enclosed with the square
           brackets []. Python lists are mutable type its mean we can modify its element after it created.


  b)Tuple:-Python Tuple is used to store the sequence of immutable Python objects. The
           tuple is similar to lists since the value of the items stored in the list can be changed,
           whereas the tuple is immutable, and the value of the items stored in the tuple cannot be 
           changed.
  
  c)Set:-A Python set is the collection of the unordered items. Each element in the set must
         be unique, immutable, and the sets remove the duplicate elements. Sets are mutable which means
         we can modify it after its creation.

  Unlike other collections in Python, there is no index attached to the elements of the set, i.e.,
  we cannot directly access any element of the set by the index. However, we can print them all
  together, or we can get the list of elements by looping through the set. 

  d)Dictionary:-Python Dictionary is used to store the data in a key-value pair format. The 
                dictionary is the data type in Python, which can simulate the real-life data arrangement where
                some specific value exists for some particular key. It is the mutable data-structure. The 
                dictionary is defined into element Keys and values.

Keys must be a single element
Value can be any type such as list, tuple, integer, etc.

In other words, we can say that a dictionary is the collection of key-value pairs where the value 
can be any Python object. In contrast, the keys are the immutable Python object, i.e., Numbers, 
string, or tuple. 
'''
#*********LIST*************

print('\n\t\t###### LIST ######')

l=[]      # an empty list
l1=list() # an empty list
l=[10,20,30]
ch='y'
while ch=='y' or ch=='Y':
    l1.append(int(input('Enter a number: ')))
    ch=input('Do you want more ? (y/n): ')
print('List l1 :',l1)
print('Reverse list is:',l1[::-1])
print('Sorted list is :',sorted(l1))
print('Length is ',len(l1))
l2 = [x*2 for x in l1 ]                   #list comprehension for getting double of elemnts from l1
print('Doubled list is:',l2)
l3 = [x**2 for x in l1 if x%2==1]         # list comprehesnion for getting squares of odd value elements from l1
print('Square of odd Values is:',l3)
print('Help on list class',dir(list))

#***********SET*************

print('\n\t\t###### set ######')

s=set()                        # an empty set
sd={}                          # its an empty dictionary and not an empty set
s={1,2,3,1,1,2,4,5}            # duplicate values will be removed
print('Set 1 is:',s)
s1={4,5}
print('Set2 is:',s1)
print('Union of set1 and Set2 is:',s.union(s1))
print('Intersection of Set1 and Set2 is:',s.intersection(s1))
print('Is Set2 subset of Set1 ? :',s1.issubset(s))
print('Help on set class :',dir(set))


#*********Tuple********

print('\n\t\t###### Tuple ######')

t=()                               # an empty tuple
t1= tuple()
t=(1,2,3,'aiktc',9.2)             # a new object would be created since tuple is immutable
print('Tuple is',t)
print('Occurences of 2 is :',t.count(2))
print('Occurences of k is :',t.count('k'))
if 'k' in t[3]:
    print('Yes')
else:
    print('No')
print('Help on tuple class:',dir(tuple))


#********* Dictinonary ********

print('\n\t\t###### Dictionary ######')

d={1:''}
d1=dict()
d.update({1:'FE'})
d.update({2:'SE'})
print('Dictionary is:',d)
l=d.items()
for i in l:
    print(i)
print('Value of given key is ',d.get('SE')) # returns none as SE is not declared
print('Keys of Dictionary :',d.keys())
print('Values in Dictionary :',d.values())
print('Help on Dictionary class',dir(dict))

'''
OUTPUT:

                ###### LIST ######
Enter a number: 90
Do you want more ? (y/n): y
Enter a number: 15
Do you want more ? (y/n): y
Enter a number: 30
Do you want more ? (y/n): n
List l1 : [90, 15, 30]
Reverse list is: [30, 15, 90]
Sorted list is : [15, 30, 90]
Length is  3
Doubled list is: [180, 30, 60]
Square of odd Values is: [225]
Help on list class ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

                ###### set ######
Set 1 is: {1, 2, 3, 4, 5}
Set2 is: {4, 5}
Union of set1 and Set2 is: {1, 2, 3, 4, 5}
Intersection of Set1 and Set2 is: {4, 5}
Is Set2 subset of Set1 ? : True
Help on set class : ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', 
'__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
'__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update'
, 'union', 'update']

                ###### Tuple ######
Tuple is (1, 2, 3, 'aiktc', 9.2)
Occurences of 2 is : 1
Occurences of k is : 0
Yes
Help on tuple class: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

                ###### Dictionary ######
Dictionary is: {1: 'FE', 2: 'SE'}
(1, 'FE')
(2, 'SE')
Value of given key is  None
Keys of Dictionary : dict_keys([1, 2])
Values in Dictionary : dict_values(['FE', 'SE'])
Help on Dictionary class ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 
'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

'''

'''
CONCLUSION: In this perticular experiment we have sucessfully mplemented data type like list,
            set, tuplet, and directory.
            list in Python is used to store the sequence of various types of data and Python Tuple is used
            to store the sequence of immutable Python objects,A Python set is the collection of the unordered 
            items.
            Each element in the set must be unique, immutable, and the sets remove the duplicate elements, 
            while.
            Python Dictionary is used to store the data in a key-value pair format.
'''