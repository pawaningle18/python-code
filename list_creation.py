
# 1. Using square brackets
list1 = [1, 2, 3, 4, 5]  
list2 = ["apple", "banana", "cherry"]  
list3 = [1, "hello", 3.14, True]  

print("List1:", list1)  
print("List2:", list2)  
print("List3:", list3)  

# 2. Using the list() constructor
tuple_data = (10, 20, 30)
list4 = list(tuple_data)
string_data = "OpenAI"
list5 = list(string_data)

print("List4 from tuple:", list4)  
print("List5 from string:", list5)  

# 3. Creating a list with repeated elements
list6 = [0] * 5
print("List6 with repeated zeros:", list6)  

# 4. Creating list with list comprehension
# e.g. squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares list:", squares)

