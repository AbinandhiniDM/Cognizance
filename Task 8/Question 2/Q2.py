# Question 2
import numpy as np
n=int(input("Enter array length:")) # Getting length of array from user

# Iniatilizing empty arrays
A=[] 
B=[]

print("Enter elements for First Array:")

# Getting elements from user
for i in range(n):
    e=int(input("Element :"))
    A.append(e)
print()    
print("Enter elements for Second Array:")   
for j in range(n):
    e1=int(input("Element :"))
    B.append(e1)

# Changing it into numpy array    
A=np.array(A)
B=np.array(B)
print()
print("First array: ",A)
print("Second arrary: ",B)
print()
# np.array_equal compares both the array and return boolean value
print(np.array_equal(A, B)) 
    

 