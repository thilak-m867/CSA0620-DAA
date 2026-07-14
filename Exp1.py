print("192572046 \nShree Thilak Muthukrishna\n")

#Linear Search (Iterative)

input = [10, 25, 30, 45, 50]
key = 30
index = 0

for i in range(0, len(input)):
    if (input[i]==key):
        print(f"Key found at index: {i}")
        break

