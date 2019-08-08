row = int(input())
col = int(input())

for i in range(row):
    for j in range(col):
        if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print(u"\u2661",end=" ")
        else:
            print(end="  ")
    print()

    #2661 2665 2764 2765 2766 2767