n = int (input("Enter no:"))
for i in range(n-1):
    for j in range(n):
        if(i==j):
            print("*",sep=" ",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if (i+j==n-1):
            print("*", sep=" ", end=" ")
        else:
            print(" ", end=" ")

    print()
for i in range(n-1,0,-1):
    for j in range(n):
        if (i == j):
            print("*", sep=" ", end=" ")
        else:
            print(" ", end=" ")
    for j in range(n):
        if (i + j == n - 1):
            print("*", sep=" ", end=" ")
        else:
            print(" ", end=" ")

    print()

