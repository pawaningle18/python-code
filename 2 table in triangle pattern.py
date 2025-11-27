rows = int(input("Enter number of rows: "))
num = 2  # start from 2

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()

