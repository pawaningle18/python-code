# Create a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Remove a value
my_list.remove(30)  # removes the first occurrence of 30
print("List after removing 30:", my_list)

# Try removing a value not in the list
try:
    my_list.remove(100)
except ValueError as e:
    print("Error:", e)

