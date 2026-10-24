
# Question 1: Write a NumPy program to convert a list of numeric
# values into a one-dimensional NumPy array.

import numpy as np

numbers = [10, 20, 30, 40, 50]
arr = np.array(numbers)

print("List:", numbers)
print("NumPy Array:", arr)
print("Dimension:", arr.ndim)






# Question 2: Write a program to demonstrate split functions
# in a NumPy array.


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
parts = np.split(arr, 3)
print("Original Array:", arr)
print("Split Arrays:")
for part in parts:
 print(part)


 # Question 3: Write a program to demonstrate slicing functions
# in a NumPy array.


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original Array:", arr)
print("Elements from index 1 to 4:", arr[1:5])
print("First three elements:", arr[:3])
print("Last three elements:", arr[-3:])



# Question 4: Write a program to demonstrate the unique function
# in a NumPy array.
import numpy as np
arr = np.array([10, 20, 20, 30, 40, 40, 50])
unique_values = np.unique(arr)
print("Original Array:", arr)
print("Unique Values:", unique_values)