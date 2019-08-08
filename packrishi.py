for i in range(5):
    for j in range(n):
        if(j==0 or i==0 or (j==n-1 and i<n//2) or (i>n//2 and i==j) or i==n//2): #R
            print("*",end=" ")
        else:
            print(" " ,end=" ")

    print()