# Number to check
num = 121

# Convert number to string
num_str = str(num)

# Check if palindrome
if num_str == num_str[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")

