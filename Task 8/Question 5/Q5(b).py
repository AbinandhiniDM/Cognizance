
# Question 5

# 2
# Getting the positions (indexes) where elements of 2 numpy arrays match

import numpy as np
n=int(input("Enter array length:")) # Getting length of the array from user
# Initializing empty arrays
arr1=[]
arr2=[]
#Gettimg elements from user
print("Enter elements for First Array:")
for i in range(n):
    e=int(input("Element :"))
    arr1.append(e)
print()    
print("Enter elements for Second Array:")   
for j in range(n):
    e1=int(input("Element :"))
    arr2.append(e1)

# Changing it into numpy arrays   
arr1=np.array(arr1)
arr2=np.array(arr2)
print()
print("First array: ",arr1)
print("Second array: ",arr2)
print()
l=[]
for i in range(n):
    if arr1[i]==arr2[i]: # Comparing both the arrays
        l.append(i) # Appending the index to the list

print("Indexex at which elements of arrays match are: ")
for i in l:
    print(i,end=" ") # Printing the indexes(position)

