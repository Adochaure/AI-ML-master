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


# Array properties helps you understand and manipulate data in arrays efficientl

arr = np.array([[1,2,3],[4,5,6]])
print(arr.ndim)  # Output: 2 (number of dimensions)]
print(arr.shape)  # Output: (2, 3) (shape of the array)
print(arr.size)  # Output: 6 (total number of elements in the array)
print(arr.dtype)  # Output: int64 (data type of the array elements)
print(arr.itemsize)  # Output: 8 (size in bytes of each element in the array)

# We can also explicitly change the             for our arrays. 
# Specify dtype at creation  
str_arr = np.array([1, 2, 3], dtype="U")  
print(str_arr, str_arr.dtype)  
float_arr = np.array([1, 2, 3], dtype="float64")  
print(str_arr, float_arr.dtype)  
# Creating new array with a specific type from existing array  
int_arr = float_arr.astype(np.int64)  
print(int_arr, int_arr.dtype) 


#operations on array

#1.Reshaping and flattening arrays
arr1 = np.array([1, 2, 3,4,5,6])
print(arr1.shape)  #(6,)
reshaped = arr1.reshape((2, 3)) # converts (1x6) => (2x3) 
print(reshaped, reshaped.shape) 
#[[1 2 3]
#  [4 5 6]] 
flattended = reshaped.flatten() # converts (2x3) => (1x6)
print(flattended, flattended.shape)  #[1 2 3 4 5 6] (6,)


#2.indexing

# Indexing for 1D array  
arr = np.array([1, 2, 3, 4, 5])  
print(arr[0])  
# Indexing for 2D array  
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) # 2D array 
print(arr[0][1]) # 2  
print(arr[1][2]) # 6 

# Fancy Indexing  
arr = np.array([1, 2, 3, 4, 5])  
idx = [0, 1, 4]  
print(arr[idx])  

arr3 = np.array([1, 2, 3, 4, 5])  
# Boolean Indexing  
print(arr3[arr3 > 2])    #[3 4 5]
print(arr3[arr3 % 2 == 0])  #[2 4]


#3.Slicing


# Slicing 1D array  
arr = np.array([1, 2, 3, 4, 5, 6, 7])  
print(arr[2:6])  # [3, 4, 5, 6]  
print(arr[:6])  # [1, 2, 3, 4, 5, 6]  
print(arr[3:])  # [4, 5, 6, 7]  
print(arr[::2])  # [1, 3, 5, 7] 

#Copy vs view
# Views are fast and memory-efficient (no data duplication). 
# Copies are safe but slower and use more memory. 

# Sliced List is a COPY  
py_list = [1, 2, 3, 4, 5]  
copy_list = py_list[1:4] # [2, 3, 4]  
copy_list[1] = 333  
print(copy_list) #[2, 333, 4] 
print(py_list) # [1, 2, 3, 4, 5] - remains same  

# Sliced Array is a VIEW  
np_arr = np.array([1, 2, 3, 4, 5])  
view_arr = np_arr[1:4] # [2, 3, 4]  
view_arr[1] = 333 
print(view_arr)  #[  2 333   4]
print(np_arr) # [1, 2, 333, 4, 5] - changes 

#Creating copy of array

copy_arr = np_arr[1:4].copy() # 2,3,4
copy_arr[1] = 555

print(copy_arr)  #[  2 555   4]
print(np_arr)    #[  1   2 333   4   5]


#multdiamesional arrays
arr1D = np.array([1,2,3])
print(arr1D.ndim) # 1 

# 2D array (matrix)  
arr2D = np.array([[1, 2, 3],  
[4, 5, 6]])  
print(arr2D.ndim) # 2  

# 3D array (tensor)  
arr3D = np.array([[[1, 2, 3],  
[4, 5, 6]],  
[[7, 8, 9], 
[10, 11, 12]]]) 
print(arr3D.ndim) # 3 

#Operations along axes
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(np.sum(arr2D))  # sum of entire array - 45 

sum_of_columns = np.sum(arr2D, axis = 0)  
print(sum_of_columns) # [12 15 18]  

sum_of_rows = np.sum(arr2D, axis = 1) 
print(sum_of_rows) # [6 15 24] 

# 1D array has 1 axis (axis0). 
# 2D array has 2 axes (axis0 = columns, axis1 = rows) 
# 3D array has 3 axes (axis0 = depth/layer, axis1 = rows in each layer, axis2 = 
# columns in each layer) 


#Operation on 3D arrays
arr3D = np.array([[[1, 2],[3, 4],[5, 6]], [[7, 8],[9, 10],[11, 12]]]) 
print(arr3D, arr3D.shape) 
# Indexing  
print(arr3D[0][1][1]) # 4  
print(arr3D[1][2][1]) # 12  
print(arr3D[:, :, 0])  # first col from both layers  
print(arr3D[:, 0, :])  # first row from both layers  
# Manipulating data  
arr3D[:, 0, :] = 99  
# change first row to store 99  
print(arr3D) 


# Common Data Types  
arr = np.array([1, 2, 3, 4, 5])  
arr2 = np.array([1.0, 2.0, 3.0])  
arr3 = np.array(["hello", "world", "prime", "ai/ml"])  
print(arr.dtype) # int64 
print(arr2.dtype) # float64  
print(arr3.dtype) # U  
# Complex Numbers  
arr1 = np.array([2 + 3j])  
arr2 = np.array([5 + 8j])  
print(arr1, arr1.dtype)  
print(arr1 + arr2)  
print(arr2 - arr1)  
# Objects  
arr = np.array (["hello", {1, 2, 3}, 3.14])  
print(arr, arr.dtype)



# np.int8 use 1byte per element, np.int16 uses 2 bytes, np.int32 uses 4 bytes, and np.int64 uses 8 bytes.

# np.int64 
# ◦ Smaller types = faster computations. 
# • Compatibility 
# ◦ Images often use 
# np.uint8 
# ◦ ML libraries expect 
# float32 


#Vectorization & Broadcasting in Numpy
#this are most powerfull feature for fast numerical computation

# Vectorization 
# Vectorization means performing operations on entire arrays at once without explicit 
# Python loops.  

# NumPy uses C-level implementations internally → much faster than Python loops. 

arr = np.array([1, 2, 3, 4, 5])  

sq_arr = arr**2  # Square of all nums 
print(sq_arr)  
arr2 = np.array([6, 7, 8, 9, 10])  
print(arr + arr2)  
# Sum of 2 arrays 


# -------------------------------------------------------------
#BROADCASTING -> automatically expand arrays of diffrent shapes
# useful for combining arrys of diff. diamension

# shape right-> left comparison
#all diamension must either be : Equal or 1 or missing

# Broadcasting with a Scalar  
arr_mul10 = arr * 10 # Multiply by 10 to all nums  
print(arr_mul10)  
# Broadcasting with a Vector  
arr1D = np.array([1, 2, 3])  
arr2D = np.array([[1, 2, 3], [4, 5, 6]])  
print(arr1D + arr2D) 

#Standard Vector Normalization
arr = np.array([[1, 2], [3, 4]])  
mean = np.mean(arr)  
std_dev = np.std(arr)  
normalized_arr = (arr - mean) / std_dev  
print(normalized_arr) 

# [[-1.34164079 -0.4472136 ]
#  [ 0.4472136   1.34164079]]


#Aggregate Functions
arr = np.array([1,2,3,4,5])
print(np.sum(arr))  # Output: 15
print(np.mean(arr))  # Output: 3.0
print(np.max(arr))  # Output: 5
print(np.argmax(arr))  # Output: 4 (index of max element)
print(np.min(arr))  # Output: 1
print(np.argmin(arr))  # Output: 0 (index of min element)
print(np.median(arr))  # Output: 3.0
print(np.std(arr))  # Output: 1.4142135623730951 standard deviarion
print(np.var(arr))  # Output: 2.0 variance

#Power functions
print(np.square(arr))  # [1, 4, 9, 16, 25] 
print(np.sqrt(arr))  
# [1, 1.41, 1.73, 2, 2.23]  
print(np.pow(arr, 3))  # [1, 8, 27, 64, 125] 

#Log & Exponential Functions
# 1. log() - returns natural log 
# 2. log10() return log base 10
# 3. log2() - returns log base 10 - returns log base 2 
# 4. exp(x) - returns e^x 

#Rounding Functions
print(np.round(2.678)) # 3.0  roundoff to nearest integer
print(np.floor(2.678)) # 2.0  round down
print(np.ceil(2.678))  # 3.0  round up
print(np.trunc(2.678)) # 2.0  truncate towards zero -> remove fractional part


arr = np.array([1, 2, -5, 3, 8, -4, 2, 5])
print(np.abs(arr))  # [1 2 5 3 8 4 2 5]
print(np.sort(arr))  # [-5 -4 1 2 2 3 5 8] 
print(np.unique(arr))  # [-5 -4 1 2 3 5 8]