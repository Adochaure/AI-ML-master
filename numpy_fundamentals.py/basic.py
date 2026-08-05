import numpy as np
#Numpy is an open-source library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. Numpy is widely used in data science, machine learning, and scientific computing due to its performance and ease of use.

#Numpy introduces new data structure called ndarray (n-dimensional array), which is a powerful and flexible way to store and manipulate data. It allows for efficient operations on large datasets, making it a fundamental tool for numerical computing in Python.

#fetures of numpy:
#Multidiamensional arrays:1D,2D,3D
#mathematical functions: sin, cos, exp, log, etc.
#vectorization: element-wise operations on arrays without explicit loops
#interoperability: seamless integration with other libraries like pandas, matplotlib, and scikit-learn

arr = np.array([1,2,3])
print(arr) # Output: [1 2 3]

#numpy array are faster than pyhton list
#stores in contiguous memory locations
#they are homogenous
#they use vectorized operation


#List vs Numpy Array

#performance comparison

import time  
size = 50_000  #dataset size
#python list
python_list = list(range(size))
start =time.time()
list_squared = [x**2 for x in python_list] # square of all nums 
end =time.time();
print("Python list time:", end - start, "seconds")  

#numpy array
numpy_arr = np.array(python_list)
start = time.time()
numpy_squared = numpy_arr ** 2  # square of all nums using vectorized operation     
end = time.time()
print("Numpy array time:", end - start, "seconds")

#results:
# Python list time: 0.0189974308013916 seconds
# Numpy array time: 0.0 seconds


#memory comparison
import sys
print("Python list size:", sys.getsizeof(python_list) * len(python_list)) 
print("NumPy array size:", numpy_arr.nbytes) 
# Python list size: 20002800000
# NumPy array size: 400000

