total = 100
def check_avail(n):
    while total<0:
        if(n<total):
            total-=n
            return True

        else:
            return False
n = int(input("Enter the no of tickets to be book:"))

if check_avail(n):
    print("Tickets available!")
else:
    print("Sorry")