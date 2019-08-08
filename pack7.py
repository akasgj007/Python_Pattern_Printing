class myclass(list):
    def remove(self,value):
        if value in self:
            i = self.index(value)
            self.pop(i)

s = map(int,input().split())
s = myclass(s)
print(s)
k = int(input("Enter k"))
s.remove(k)
print(s)