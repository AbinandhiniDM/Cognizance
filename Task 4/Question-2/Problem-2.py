# Question 2

s=input("Enter a string:") # Getting string from user

# Method 1
# Using for loop
n=len(s)
print("Printing the result using Method 1")
for i in range(0,n,2):
    print(s[i],end='')
print()

# Method 2
# Using string slicing
print("Printing the result using Method 2")
print(s[::2])