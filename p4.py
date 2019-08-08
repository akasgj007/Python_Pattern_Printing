l = list(map(int,input().split(" ")))
n = len(l)
i,j,s1,s2,flag = 0,n-1,l[0],l[n-1],0
while(i<j):
    if(i+1==j-1 and s1==s2):
        print ("Equillbrium is ",l[j-1])
        print (l[:j-1],l[j:])
        flag=1
        break
    elif(s1<s2):
        i+=1
        s1+=l[i]
    else:
        j-=1
        s2+=l[j]

if flag==0:
    print("Equillibrium not exists")