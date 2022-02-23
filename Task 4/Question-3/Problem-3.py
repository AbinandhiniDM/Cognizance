# Question 3

print("i) Adding records and printing them")
r1=['Roll no','Name','Marks']
r11=['1','Abc','90']
l=[r1,r11]

# i)
n=int(input("Enter how many records you want to add:")) # Getting no.of records to add
for i in range(n):
    print()
    print('Record number',i+1)
    d1=input("Enter Rollno:")
    d2=input("Enter name:")
    d3=input("Enter Marks:")
    r2=[d1,d2,d3]
    l.append(r2) # Adding each record to 2D list
print()
print("Printing the list")
print()
for i in l: # Printing the list
    if i[0]=='Roll no':
        print(i[0]+'   '+i[1]+'   '+i[2])
    else:
        print(3*' '+i[0]+3*'  '+i[1]+3*'  '+i[2])

# ii)
print()
print("ii) Printing second row/record")
if len(l)<3:
    print("The no of record is less than 2")
else:
   # print("Second record/row")
    print(l[2][0]+'  '+l[2][1]+'  '+l[2][2]) # Printing second row/record