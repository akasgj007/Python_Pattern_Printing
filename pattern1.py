n=int(input("Enter no:"))
m = 18
num = 65
for i in range(n):
    for j in range(m):
        print(end=" ")
    m-=1
    for j in range(i+1):
        print(chr(num),end=" ")
        num+=1
    print(" ")