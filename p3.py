#mapping method
#l = input().split(" ")
#l1 = list(map(int,l))
#print(l1)
def checksum (lis):
    sum = 0
    for i in range (len(lis)):
        sum = sum + lis[i]
    return sum

sum1 = 0
l = input().split(" ")
n = len(l)
l = list(map(int,l))
for i in range(n-1) :
    sum1 = sum1 + l[i]
    sum2 = checksum(l[i+2:])
    if sum1 == sum2 :
        #print (sum1)
        print (l[:i+1],l[i+2:])
        #print (l[i+2:])
    else :
        print ("Equillibirum not exits")
    i+=1


