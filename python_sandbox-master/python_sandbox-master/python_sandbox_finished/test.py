# This is a list of fruits
fruits = ['oranges', 'apple', 'grape', 'banana']
print(fruits)
# This function displays the function of a list
# This function add an element (guava) to the end of a list
fruits.append('guava')
print(fruits)
# This method removes the last element of a list
fruits.pop()
print(fruits)
# This function removes the 4th element in a list
fruits.pop(3)
print(fruits)
# This function removes all the elements in a list
# fruits.clear()
# print(fruits)
# This function gets or targets the 2nd element in a list
print(fruits[1])
print(fruits)

fruits.insert(1, 'Grape')
print(fruits)

phones = ['iPhone', 'Samsung', 'Tecno', 'Itel', 'Huawei']
phones_and_fruits = phones+fruits
print(phones_and_fruits)
phones_and_fruits.remove('Samsung')
print(phones_and_fruits)


phones_and_fruits.sort()
print(phones_and_fruits)
phones_and_fruits.sort(reverse=True)
print(phones_and_fruits)
print(len(phones_and_fruits))

# THIS IS USED TO GET A CERTAIN PORTION OF A LIST
print(phones_and_fruits[0:5])
