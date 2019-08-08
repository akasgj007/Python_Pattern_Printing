m=(2*10)-2
for i in range(1,10):
  for j in range(m):
    print(end=" ")
    for i in range(0,i,1):
        print(2**i ,end=" ")
    for i in range(-1+i,-1,-1):
        print(2**i,end=" ")
  print(" ")