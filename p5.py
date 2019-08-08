"""#Moser De Brujin Sequence
n = int(input())
l=[0,1]
i=1
while(len(l)<=n):
    l.append(l[i]*4)
    l.append(l[i]*4+1)
    i+=1
print(l)
print(l[n])
"""
"""def gen(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n%2==0:
        return 4 * gen(n//2)
    else:
        return 4 * gen(n//2) + 1

def check(n):
    for i in range(0):
        print(gen(i),end=" ")

print (check(n))
"""
""""
"""
"""str = input()
print (int(str,base=17))
"""
"""
#find the given term of that number
n = int(input())
m = list(map(int,bin(n)[2:]))
print(m)
m.reverse()
print(m)
l= len(m)
print(l)
s=0
for i in range(l):
    s=s+m[i]*(4**i)
print (s)
"""
"""
n=int(input())
#n = int(bin(s)[2:],base=4)
#print(int(bin(int(input()))[2:],base=4))
#another method
n=list(bin(n)[2:])
n='0'.join(n)

print(n)
"""
n=int(input())
n=bin(n)[2:]
s=n[1::2]
if(s!=None or int(s)==0):
    print("position of %d is %d"%(n,int(n[::2],base=2)))
else:
    print("Not Present")