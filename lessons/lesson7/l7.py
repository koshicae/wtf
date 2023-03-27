# try, except
#
# try:
#     print(x)
# except:
#     print('The x is not declared')

# Multiple exceptions
# try:
#     print(x)
# except NameError:
#     print('Variable x is not defined')
# except:
#     print('Something else went wrong')

# print(ell) - IndentationError
#
# try:
#     print('Hello')
# except:
#     print('Something went wrong')
# else: # # No errors
#     print('Nothing went wrong')
#
# try:
#     print(x)
# except:
#     print('Something went wrong')
# finally:  # Will do whatever happens, even he is right or wrong, he doesn't give a s
#     print("The 'try except' is finished")

# # Declare a class
# class MyPet():
#     # declare parameters (свойства)
#     name = ''
#     age = 1
#
# # Create an object
# dog = MyPet()
#
# # Print parameters
# print(dog.name)
# print(dog.age)
#
# # Change parameters
# dog.name = 'Rex'
# dog.age = 23
#
# # Print parameters
# print(dog.name)
# print(dog.age)

# Declare a class
# class Person:  # ! doesn't always require ()
#     # declare parameters with __init__
#     def __init__(self, name, age):  #always self
#         self.name = name
#         self.age = age
#
# p1 = Person('Ion', 16)
#
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age
#
# p1 = Person('Mihai', 14)
#
# print(p1.name)
# print(p1.age)

# class Person:
#     # declare parameters wuth __init__
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('Hi my name is', self.name, 'and I am', self.age, 'years old')
#
# p1 = Person('Ion', 16)
# p1.say_hi()