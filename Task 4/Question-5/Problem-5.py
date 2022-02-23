# Question 5
n=int(input("Enter no.of rows:")) # Getting no.of rows from user
x=n-1
for i in range(0,n):
    for j in range(0, x): # For space at beginning
        print(end=" ") 
    x=x-1
    for j in range(0, i+1): # For printing each row
        print("* ", end="") 
    print() # For printing each row at next line
