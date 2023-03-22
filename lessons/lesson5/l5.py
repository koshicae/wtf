# array = []
#
# int_array = [3,4,5,6,7,87,8]
# char_array = ["s","a","l","u","t"]
# float_array = [5.4, 34.5, 6.2]
# bool_array = [True, False, False, True]
#
# print(int_array)
# print(char_array)
# print(float_array)
# print(bool_array)
#
# for i in range(0,6):
#     print(int_array[i])
#
# for i in range(0, len(char_array)):
#     print(char_array[i])
#
# for i in float_array:
#     print(i)
#
# for i in bool_array:
#     print(i)

# test = []
# l = int(input('Enter the array length'))
# for i in range(0,l):
#     test.append(int(input('Enter element with index ' + str(i) + '\n')))
# print(test)

# a =      [1, 1, 2, 5, 8, 13, 22, 34, 35, 2, 3]
# Index:  0  1  2  3  4  5   6   7   8   9  10
# print(a[3])
# print(a[a[3]])
# print(a[a[5]])

# a.append()	#Adds an element at the end of the list
# print(a)
# a.clear()	#Removes all the elements from the list
# print(a)
# a.copy()	#Returns a copy of the list
# print(a)
# a.count()	#Returns the number of elements with the specified value
# print(a)
# a.extend()	#Add the elements of a list (or any iterable), to the end of the current list
# print(a)
# a.index()	#Returns the index of the first element with the specified value
# print(a)
# a.insert()	#Adds an element at the specified position
# print(a)
# a.pop()	#Removes the element at the specified position
# print(a)
# a.remove()	#Removes the first item with the specified value
# print(a)
# a.reverse()	#Reverses the order of the list
# print(a)
# a.sort()	#Sorts the list
# print(a)

# tuple_ex = ('Hola', 5, "Test", 4.55, False) #no commands
#tuple_ex.append() #Error
# print(tuple_ex[0])
# print(tuple_ex + ("New", "data", 1))

# simple_array = [1,2,3,4,5,0,2,3,4,5,2,3]
# set_array_2 = {4,3,2,4,5,5,41,2}
# set_array = set(simple_array)
#
# print(simple_array)
# print(set_array) #no repeatables
# print(set_array_2)

# dictionary = {"Key": "Value", "Int": 3, "Float": 23.4, "Bool": True} #string все
# print(dictionary)
# print(dictionary.get('Key'))
# dictionary.update({"Int": 4})
# print(dictionary)
# dictionary["Key"] = "New Value"
# print(dictionary)

meow_num = {'cat', 7, 'mrr'}
woof_num = {'dog', 'bark', 7, 7, 7, 7, 7, 7, 7, 77}
print(meow_num.intersection(woof_num))
print(meow_num.union(woof_num))
print(woof_num)