# EXP 11: Working with NumPy arrays.
'''
 
        NAME : Saqlain Kalokhe
        ROLL : 20CO22
        YEAR : 2021-22

THEORY:
NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, 
and tools for working with these arrays. It is the fundamental package for scientific computing with Python. Numpy
is basically used for creating array of n dimensions.Reshaping numpy array simply means changing the shape of the 
given array, shape basically tells the number of elements and dimension of array, by reshaping an array we can add
or remove dimensions or change number of elements in each dimension.
'''
import numpy as np

#creating numpy arrays

#create 1D and 2D arrays using array function
arr1d = np.array([1,2])
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)

#create array using arange function
arr_ar = np.arange(1,100,9)

#create array using linspace function
arr_lp = np.linspace(10,11,10)

#create array using logspace function
arr_logp = np.logspace(10,15,10)

#create array using various functions
arr_zeros = np.zeros((2,3))
arr_ones = np.ones((3,2))
arr_empty = np.empty((2,4))
arr_identity = np.identity(3)

#accessing array elements
print('arr1d =',arr1d)
print('arr2d =')
for row in arr2d:
    print(row)
    
print('arr_ar =',arr_ar)
print('arr_lp =',arr_lp,' having size of',arr_lp.size)
print('arr_logp =',arr_logp,' having size of',arr_logp.size)
print('arr_zeros =\n',arr_zeros)
print('arr_ones =\n',arr_ones)
print('arr_empty =\n',arr_empty)
print('arr_identity =\n',arr_identity)

#performing array operations
print('\nPerforming Array Operations:')
print('Addition of 2D arrays\n',arr2d + arr_identity)
print('Substraction of 2D arrays\n',arr2d - arr_identity)
print('Multiplication of 2D arrays\n',arr2d * arr_identity)
print('Matrix Multiplication of 2D arrays\n',arr2d @ arr_identity)
print('Transpose of 2D arrays\n',arr2d.transpose())

#performing slice operations
print('Elements of Second Row and First 2 Columns',arr2d[1,:2])
print('Elements of Last Row and Second Column onwards',arr2d[-1,1:])
print(arr2d[arr1d])

#performing reshape on arrays

# The meaning of reshape is "to change the dimension of metrix i.e array."
# there are two way to change the dimension of array.

# creating a numpy 1D-array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print("Array : " + str(array))
# length of array
n = len(array)
N = 4
M = n//N        #floor division

# First way 
# converting 1D array to 2-D array
reshaped1 = array.reshape((N, M))
# N is number of rows. M is number of columns.

# printing reshaped array
print("First Reshaped 2D Array : ")
print(reshaped1)

# Second way
reshaped2 = np.reshape(array, (2, 8))
# printing reshaped array
print("Second Reshaped 2D Array : ")
print(reshaped2)


# converting 1D array to 3-D array
reshaped = array.reshape((2, 2, 4))
print("Reshaped 3-D Array : ")
print(reshaped)


# converting 2-D array to 1-D array
array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print(" 2-D Array : ")
print(array)
reshaped = array.reshape((9))
# 9 is number of columns.
print("Reshaped 1-D Array : ")
print(reshaped)

# or we can use unknown dimension
# reshaped = array.reshape((-1))

'''
OUTPUT:
arr1d = [1 2]
arr2d =
[1. 2. 3.]
[4. 5. 6.]
[7. 8. 9.]
arr_ar = [ 1 10 19 28 37 46 55 64 73 82 91]
arr_lp = [10.         10.11111111 10.22222222 10.33333333 10.44444444 10.55555556
 10.66666667 10.77777778 10.88888889 11.        ]  having size of 10
arr_logp = [1.00000000e+10 3.59381366e+10 1.29154967e+11 4.64158883e+11
 1.66810054e+12 5.99484250e+12 2.15443469e+13 7.74263683e+13
 2.78255940e+14 1.00000000e+15]  having size of 10
arr_zeros =
 [[0. 0. 0.]
 [0. 0. 0.]]
arr_ones =
 [[1. 1.]
 [1. 1.]
 [1. 1.]]
arr_empty =
 [[0.00e+000 0.00e+000 0.00e+000 0.00e+000]
 [0.00e+000 1.54e-321 0.00e+000 0.00e+000]]
arr_identity =
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Performing Array Operations:
Addition of 2D arrays
 [[ 2.  2.  3.]
 [ 4.  6.  6.]
 [ 7.  8. 10.]]
Substraction of 2D arrays
 [[0. 2. 3.]
 [4. 4. 6.]
 [7. 8. 8.]]
Multiplication of 2D arrays
 [[1. 0. 0.]
 [0. 5. 0.]
 [0. 0. 9.]]
Matrix Multiplication of 2D arrays
 [[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]
Transpose of 2D arrays
 [[1. 4. 7.]
 [2. 5. 8.]
 [3. 6. 9.]]
Elements of Second Row and First 2 Columns [4. 5.]
Elements of Last Row and Second Column onwards [8. 9.]
[[4. 5. 6.]
 [7. 8. 9.]]
Array : [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
First Reshaped 2D Array :
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
Second Reshaped 2D Array :
[[ 1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16]]
Reshaped 3-D Array :
[[[ 1  2  3  4]
  [ 5  6  7  8]]

 [[ 9 10 11 12]
  [13 14 15 16]]]
 2-D Array :
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Reshaped 1-D Array :
[1 2 3 4 5 6 7 8 9]

CONCLUSION:
        We have successfully implement numpy library in our Program. We have learned the ways to declare an array using numpy.
        We have learned how to change the dimension of array using reshape method of numpy.
'''