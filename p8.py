import itertools
n = int(input())
l = [i for i in range(1,n+1)]
print(l)
l3=[]
l2=list(itertools.permutations(l))
print(l2)
print(len(l2))
for i in l2:
    for j in range(n):
        if (i[j]==l[j]):
            break
        else:
            l3.append(i)
            break

print(l3)
print(len(l3))