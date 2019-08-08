n = 5
for i in range(5):
    for j in range(n):
        if(i==0 or i+j==n-1 or i==n-1):
          print("*",end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=' ')
    for j in  range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=' ')
    for j in range(n):
        if(j==0 or j==n-1 or i==n//2):
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print(" ",end=' ')
    for j in range(n):
        if (i == 0 or j == 0 or i == n - 1 or j == n - 1):
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()