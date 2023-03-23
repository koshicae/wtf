# num = int(input('Введите номер:'))
# temp = num
# rev = 0
# while num > 0:
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10
# if temp == rev:
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")


# Function declaration
# def test(): # def = definition
    # Function block
    # print('This is test')

# Function call
# test()

# Function declaration with parameters
# def calc(a, b): # parameters = (a, b)
    # print(a + b)
    # print(a - b)
    # print(a * b)
    # print('')

# calc(3, 4) # parameters = (3, 4)
# calc(5, 8)
# calc(3, 4)
# calc(4, 9)


# Function declaration with initial values
# def meow(a, c, b=5):
#     print(a + b)
#     print(a - b)
#     print(a * b)

# Function call; Send arguments
# meow(4)
# meow(5, 8)

#++++
# string=input(("Enter a string:"))
# print(string)
# string2=string[::-1]
# print(string2)
# if(string==string2):
#       print("The string is a palindrome")
# else:
#       print("Not a palindrome")


# def isPalindrome(str):
#
#     for i in range(O, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#         return False
#     return True
#
# # main function
# s = "kayak"
# ans = isPalindrome(s)
#
# if (ans):
#     print("Yes")

# else:
# 	print("No")

#Function declaration; using *args
# def arg_calc(*args):
    # *args - последний в списке, ошибку даст если поставить вначале
    # unknown > by default > *args > key:args
    # print(*args)
    # print(args)
    # print(args[0] + args[1])
    # print(args[0] * args[1])
    # print(args[0] - args[1])

#Function call
# arg_calc(3, 5)
# pycharm shortcuts


# def f_return(word):
#     return word.upper()
# in_word = input('Write any word: ')
# up_word = f_return(in_word)
# print(up_word)

#Print numbers from 1 to 10
# for i in range(1,10):
#     print(i)
# print('')
# #Print numbers from 1 to 10 without 4
# for i in range(1,10):
#     if i == 4:
        # continue #cycle start again; пропускать итерацию (команды после), идти дальше по списку
    # print(i)

#Print numbers from 1 to 10 until 4
# for i in range(1, 10):
#     if i == 4:
#         break #all cycle stops
#     print(i)

# for i in range(1, 10):
#     if i == 4:
#         print('meow')
#         pass # nothing happens
#     print(i)