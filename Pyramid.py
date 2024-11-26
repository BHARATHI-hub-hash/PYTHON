#Pyramid start from 0
n=1
# for loop for creating Rows and Columns
for row in range(1,21): # Loop for rowa from 1 to 20
    for col in range(row): # Loop for numbers in each rows
        if n>=21: # If number exceed 20 need break to stop
            break
        print(n,end="  ") # print n
        n +=1 # Increase the n
    print()
    if n>=21:
     break # stop if the number exceed 20