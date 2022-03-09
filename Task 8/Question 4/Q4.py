
# Question 4

import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' , 'chennai' , 'campus'])
ser=ser.str.title() # Capitalizing first letter of each element using title()
for i in ser:
    print(i,end=" ") # Printing the series

