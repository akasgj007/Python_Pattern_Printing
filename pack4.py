#inherited class
class A1:
    val = "Hello"
    def print(self):
        print(self.val)
class B1(A1):
    pass
obj = B1()
obj.print()