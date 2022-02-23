# Question 1
"""a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=a+b
print("The sum of two numbers is: ",c)"""


# Question 2
"""s=input("Enter a string:")
n=len(s)
for i in range(0,n,2):
    print(s[i],end='')"""
    
# Question 3
r1=['Roll no','Name','Marks']
l=[r1]
n=int(input("Enter how many records you want to add:"))
# i)
for i in range(n):
    print()
    print('Record number',i+1)
    print()
    d1=input("Enter Rollno:")
    d2=input("Enter name:")
    d3=input("Enter Marks:")
    r2=[d1,d2,d3]
    l.append(r2)
for i in l:
    if i[0]=='Roll no':
        print(i[0]+'   '+i[1]+'   '+i[2])
    else:
        print(3*' '+i[0]+3*'  '+i[1]+3*'  '+i[2])

# ii)
if len(l)<3:
    print("The no of record is less than 2")
else:
    print("Second record/row")
    print(l[2][0]+'  '+l[2][1]+'  '+l[2][2])
    
    
# Question 4
"""p=input("Enter a number:")
p1=p[::-1]
if p==p1:
    print("The given number is a Palindrome number")
else:
    print("The given number is not a Palindrome number")"""
        

# Question 5
'''n=int(input("Enter no.of rows:"))
k=n-1
for i in range(0,n):
    for j in range(0, k):
        print(end=" ")
    k=k-1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")'''