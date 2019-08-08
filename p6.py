l= list(map(int,input().split((","))))
print(l)
n = int(input("Enter no. to delete:"))
try:
  l.remove(n)
  print(n,"removed")
  print(l)
except:
   print("Item not list")
