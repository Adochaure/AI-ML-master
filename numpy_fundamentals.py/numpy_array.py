import numpy as np

#creating a numpy array from lists
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

arr2 = np.array([2,4,6,8,'aditya'])
print(arr2,type(arr2))  # Output: ['2' '4' '6' '8' 'aditya'] <class 'numpy.ndarray'>    

#2D array
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d,arr_2d.shape)  # Output: [[1 2 3] [4 5 6]] (2, 3)


#2.using Built in functions

arr1 = np.zeros((2,3))
print(arr1,arr1.shape)  # Output: [[0. 0. 0.] [0. 0. 0.]] (2, 3)

arr2 = np.ones((2,3))   
print(arr2,arr2.shape)  # Output: [[1. 1. 1.] [1. 1. 1.]] (2, 3)

arr3=np.full((2,3),7)
print(arr3,arr3.shape)  # Output: [[7 7 7] [7 7 7]] (2, 3)

arr4 = np.eye(5) #identity matrix of 5X5
print(arr4,arr4.shape)  # Output: [[1. 0. 0. 0. 0.] [0. 1. 0. 0. 0.] [0. 0. 1. 0. 0.] [0. 0. 0. 1. 0.] [0. 0. 0. 0. 1.]] (5, 5)

arr5 = np.arange(0,20,2)
print(arr5,arr5.shape)  # Output: [ 0  2  4  6  8 10 12 14 16 18] (10,)

arr6 = np.linspace(0,11,5) #5 numbers between 0 and 11
print(arr6,arr6.shape)  # Output: [ 0.    2.75  5.5   8.25 11.  ] (5,)


