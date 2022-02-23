# Question 4

p=input("Enter a number:")

# Method 1
# Using string slicing
print()
print("Printing the result using Method 1")
p1=p[::-1]
if p==p1:
    print("The given number is a Palindrome number")
else:
    print("The given number is not a Palindrome number")
    
# Method 2
print()
print("Printing the result using Method 2")
p=int(p)
temp=p
rev=0
while(p>0):
    dig=p%10
    rev=rev*10+dig
    p=p//10
if(temp==rev):
    print("The given number is a palindrome")
else:
    print("The given number isn't a palindrome")