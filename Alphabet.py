def A():
    n=5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0 or j == n - 1 or i == n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def B():
    n=5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0 or j == n - 1 or i == n // 2 or i==n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def C():
    n=5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0 or   i == n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def D():
    n=5
    for i in range(5):
        for j in range(n):
            if (j == 1 or i == 0 or   i == n-1 or j==n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def E():
    n=5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0 or   i == n-1 or i==n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    print()
def F():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0  or i == n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def G():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0 or i == n - 1 or (j==n-1 and i>n//2) or (i==n//2 and j!=1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def H():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or j==n-1 or i==n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def I():
    n = 5
    for i in range(5):
        for j in range(n):
            if (i==0 or  i==n-1 or j==n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def J():
    n = 5
    for i in range(5):
        for j in range(n):
            if (i==0 or  (i==n-1 and j<n//2) or j==n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def K():
    n = 5
    for i in range(5):
        for j in range(n//2,n):
            if (j==n//2 or (i+j==n-1 and j>n//2) or (i==j and j>n//2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def L():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or i==n-1 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def M():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or j==n-1 or (i==j and i<n//2) or (i+j==n-1 and i<=n//2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def N():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or j==n-1 or (i==j)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def O():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or j==n-1 or i==0 or i==n-1 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def P():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j == 0 or i == 0  or i == n // 2 or (j==n-1 and i<n//2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def R():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or i==0 or (j==n-1 and i<n//2) or (i>n//2 and i==j) or i==n//2 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def Q():
    n = 5
    for i in range(5):
        for j in range(n):
            if ((j==0 and i<n-1) or (j==n-2 and i!=n-1) or (i==0 and j<n-1) or (i==n-2 and j!=n-1) or (i==j and i>=n//2) ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def S():
    n = 5
    for i in range(5):
        for j in range(n):
            if (i == 0 or (j == 0 and i<n//2) or i == n//2 or i == n - 1 or (j==n-1 and i>n//2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def T():
    n = 5
    for i in range(5):
        for j in range(n):
            if (i==0 or j==n//2 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    print()
def U():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or j==n-1 or i==n-1 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def V():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or i+j==n-1 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    print()
def W():
    n = 5
    for i in range(5):
        for j in range(n):
            if (j==0 or j==n-1 or (i==j and i>n//2) or (i+j==n-1 and i>=n//2) ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
def X():
    n = 5
    for i in range(5):
        for j in range(n):
            if (i==j or i+j==n-1 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def Y():
    n = 5
    for i in range(5):
        for j in range(n):
            if ((i==j and i<n//2) or (i+j==n-1 and i<=n//2) or(j==n//2 and i>n//2) ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def Z():
    n = 5
    for i in range(5):
        for j in range(n):
            if (i==0 or i==n-1 or i+j==n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    print()



name = input("Enter the word to be print(without any spaces):")

char = list(name)
for char in char:
    if char == 'A' or char =='a':
        A()
    elif char == 'B' or char == 'b':
        B()
    elif char == 'C' or char == 'c':
        C()
    elif char == 'D' or char == 'd':
        D()
    elif char == 'E' or char == 'e':
        E()
    elif char == 'F' or char == 'f':
        F()
    elif char == 'G' or char == 'g':
        G()
    elif char == 'H' or char == 'h':
        H()
    elif char == 'I' or char == 'i':
        I()
    elif char == 'J' or char == 'j':
        J()
    elif char == 'K' or char == 'k':
        K()
    elif char == 'L' or char == 'l':
        L()
    elif char == 'M' or char == 'm':
        M()
    elif char == 'N' or char == 'n':
        N()
    elif char == 'O' or char == 'o':
        O()
    elif char == 'P' or char == 'p':
        P()
    elif char == 'Q' or char == 'q':
        Q()
    elif char == 'R' or char == 'r':
        R()
    elif char == 'S' or char == 's':
        S()
    elif char == 'T' or char == 't':
        T()
    elif char == 'U' or char == 'u':
        U()
    elif char == 'V' or char == 'v':
        V()
    elif char == 'W' or char == 'w':
        W()
    elif char == 'X' or char == 'x':
        X()
    elif char == 'Y' or char == 'y':
        Y()
    elif char == 'Z' or char == 'z':
        Z()
    else:
        print("Please print a Alphabet Letter!")