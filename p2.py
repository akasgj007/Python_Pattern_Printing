n = int(input("enter:"))
le,i=1,0
while True:
    s = bin(i)[2:]
    s = s.zfill(le)
    s = s.replace('1','9')
    s = s.replace('0', '1')
    m = int(s)
    if(m%n==0):
        print (m)
        break
i+=1

if (i==2**le):
     i=0
     le+=1
