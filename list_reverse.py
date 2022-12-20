Test_list = [1, 2, 3, 4, 5]
Test_list.reverse()
print(Test_list)  # Output:  [5,4,3,2,1]

New_list = Test_list.reverse()
print(New_list)  # Output: None




Test_list = [1, 2, 3, 4, 5]
New_list = Test_list.copy()
New_list.reverse()

print("Original List: ", Test_list)  # Output: [1,2,3,4,5]
print("Reversed List: ", New_list)  # Output: [5,4,3,2,1]

# https://www.scaler.com/topics/how-to-reverse-a-list-in-python/
