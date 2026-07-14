print("192572046\nShree Thilak Muthukrishna")

n1 = int(input("Enter n for iteration: "))
n2 = int(input("Enter n for recursion: "))

#Iteration
def fib_it(n):
    l = []
    if n >= 1:
        l.append(0)
    if n >= 2:
        l.append(1)
    
    for i in range(1, n-1):
        next_val = l[i-1]+l[i]
        l.append(next_val)
    
    return l

print("The fibonacci series using iteration is:")
for i in fib_it(n1):
    print(i, end=" ")

print("\n\n")

#Recursion 
def fib_rec(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_rec(num-1) + fib_rec(num-2)
    
fib_series = [fib_rec(i) for i in range(n2)]

for i in fib_series:
    print(i, end=" ")
    