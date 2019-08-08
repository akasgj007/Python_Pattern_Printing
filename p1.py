n = int (input("Enter the no"))
i =1
while True:
    s = bin(i)[2:]
    s  = s.replace('1','9')
    m = int(s)
    if ( m % n ==0):
        print(m)
        break
    i+=1
