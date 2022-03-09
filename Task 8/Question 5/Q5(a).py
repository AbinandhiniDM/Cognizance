
# Question 5

# 1
# Adding two arrays

import numpy as np
n=int(input("Enter array length:")) # Getting length of the array from user
# Initializing empty arrays
a1=[]
a2=[]
#Gettimg elements from user
print("Enter elements for First Array:")
for i in range(n):
    e=int(input("Element :"))
    a1.append(e)
print()    
print("Enter elements for Second Array:")   
for j in range(n):
    e1=int(input("Element :"))
    a2.append(e1)

# Changing it into numpy arrays
a1=np.array(a1)
a2=np.array(a2)
print()
print("First array: ",a1)
print("Second array: ",a2)
print()
ad=np.add(a1,a2) # Adding both the arrays using add()
print("Sum of 2 arrays: ",ad) # Printing the result


















