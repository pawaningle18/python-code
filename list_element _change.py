## Create a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Change a single element by index
my_list[2] = 300   # Change the element at index 2 (third item)
print("After changing index 2:", my_list)

# Change the last element using negative index
my_list[-1] = 500
print("After changing last element:", my_list)

# Change a slice (multiple elements)
my_list[1:3] = [200, 250]   # Replace elements at index 1 and 2
print("After slicing change:", my_list)

