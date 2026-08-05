import numpy as np

#creating a numpy array from lists
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

arr2 = np.array([2,4,6,8,'aditya'])
print(arr2,type(arr2))  # Output: ['2' '4' '6' '8' 'aditya'] <class 'numpy.ndarray'>    

#2D array
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d,arr_2d.shape)  # Output: [[1 2 3] [4 5 6]] (2, 3)
