
#Print n to 1 backwards (recursive)
def show(n):
    if (n == -1):
        return #base case
    print(n)
    show(n-1)

show(10)