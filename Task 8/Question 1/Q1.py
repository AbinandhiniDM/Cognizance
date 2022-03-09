# Question 1

import numpy as np
# Getting first and last number from user
n1=int(input("Enter first number:"))
n2=int(input("Enter last number:"))
arr=np.array([]) # Initializing empty numpy array
r=n2-n1
for i in range(r):
    arr=np.append(arr,n1) # Appending element to array
    arr=np.append(arr,(np.zeros(5))) # Adding 5 zeros after element to array
    n1+=1 # Incrementing element
arr=np.append(arr,n2) # Appending last element
print()
print(arr) # Printing the array
    

#
