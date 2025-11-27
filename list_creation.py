
list1 = [1, 2, 3, 4, 5]  
list2 = ["apple", "banana", "cherry"]  
list3 = [1, "hello", 3.14, True]  

print("List1:", list1)  
print("List2:", list2)  
print("List3:", list3)  

tuple_data = (10, 20, 30)
list4 = list(tuple_data)
string_data = "OpenAI"
list5 = list(string_data)

print("List4 from tuple:", list4)  
print("List5 from string:", list5) 

list6 = [0] * 5
print("List6 with repeated zeros:", list6)  

squares = [x**2 for x in range(1, 6)]
print("Squares list:", squares)

