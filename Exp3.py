print("192572046\nShree Thilak Muthukrishna")

n1 = int(input("Enter a number to calculate it's factorial (Iterative):"))
n2 = int(input("Enter a number to calculate it's factorial (Recursive):"))
facti = 1


#Iterative
for i in range(1, n1+1):
    facti *= i

print(f"Iterative result is :{facti}\n")

def factorial(a):
    if a>1:
        return a*factorial(a-1)
    else:
        return 1

factr = factorial(n2)

print(f"Recursive resukt is: {factr}")
