# Number to check
num = 153
sum = 0
temp = num
n = len(str(num))  # Number of digits

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

# Check if Armstrong
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

