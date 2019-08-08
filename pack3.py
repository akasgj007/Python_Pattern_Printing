
for i in range(5):
    for j in range(n):
        if(j==0 or i==0 or j==n-1 or i==n//2): #A
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=' ')

    for j in range(n//2,n):
        if(j==n//2 or (i+j==n-1 and j>n//2) or (i==j and j>n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    for j in range(n):
        if(j==0 or i==0 or j==n-1 or i==n//2): #A
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=' ')
    for j in range(n):
        if (i == 0 or (j == 0 and i<n//2) or i == n//2 or i == n - 1 or (j==n-1 and i>n//2)): #S
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=" ")
    for j in range(n):
        if(j==0 or j==n-1 or i==n//2): #H
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=' ')

    print()