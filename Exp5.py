print("192572046\nShree Thilak Muthukrishna")

r1 = int(input("Enter number of rows for matrix 1:    "))
c1 = int(input("Enter number of columns for matrix 1: "))
r2 = int(input("Enter number of rows for matrix 2:    "))
c2 = int(input("Enter number of columns for matrix 2: "))

mat1 = []
print("--- Matrix 1 Input ---")
for i in range(r1):
    row = []
    for j in range(c1):
        val = int(input(f"Enter {i+1},{j+1} element for M1: "))
        row.append(val)
    mat1.append(row)

mat2 = []
print("\n--- Matrix 2 Input ---")
for i in range(r2):
    row = []
    for j in range(c2):
        val = int(input(f"Enter {i+1},{j+1} element for M2: "))
        row.append(val)
    mat2.append(row)

mat3 = []

if c1 != r2:
    print("Matrix multiplication is not possible. Columns of M1 must equal Rows of M2.")
else:
    result = [[0 for _ in range(c2)] for _ in range(r1)]   
    for i in range(r1):         
        for j in range(c2):     
            for k in range(c1):  
                result[i][j] += mat1[i][k] * mat2[k][j]


    print("\n-----------Matrix 1------------")
    for i in mat1:
        print(i)
    print("\n-----------Matrix 2------------")
    for i in mat2:
        print(i)

    print("\n--- Result Matrix (M1 x M2) ---")
    for row in result:
        print(row)