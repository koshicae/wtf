# word
# print("Howdy, world!")
# number
# print(1)
# subtraction
# print(2 - 1)
# addition
# print(3 + 2)
# multiplication
# print(3 * 3)
# division
# print(2 / 5)
# power
# print(3 ** 3)
# integer
num1 = 1
# float
num2 = 2.4
# result = num1 + num2

message1 = "hello 1"
message2 = 'hello 1'

# mathematical operations with variables
# print(num1 + num2)
# printing the variable result
# print(result)
# concatenation
# result = message1 + message2

# print(result)

# input from user
# num3 = input("Your number:")

# print(num1 + num3)
# print(num1 + int(num3))

# name = input("Your name:")
# print('Hello, ' + name)

boolVar1 = True
boolVar2 = False

# logical OR; returns true if one true
# print(boolVar1 or boolVar2)

# logical AND; returns true if both true
# print(boolVar1 and boolVar2)

# logical NOT; reverse
# print(not boolVar1)

# float_var = 3.14
#int
# print(int(float_var))
#string
# print(str(float_var))
#bool
# print(bool(float_var))

# bool_var = True
# print (float(bool_var))

# hour = -5
# if 0 < hour < 12:
#    print('Good morning!')
# elif hour < 18:
#    print('Good afternoon!!!!')
# elif hour < 24:
#    print('Good evening!!!!')
# elif hour < 0:
#    print('kavo')
# else:
#    print('henlo')

# quit_flag = 4
# match quit_flag:
#    case True:
#       print('Quitting')
#        exit()
#    case False:
#        print('System is on')
# Подстановочный знак
#    case _:
#        print('Boolean Value was not passed')

# status = 0
#
#
# class switch:
#     on = 1
#     off = 0
#
#
# match status:
#     case switch.on:
#         print('Switch is on')
#     case switch.off:
#         print('Switch is off')

n = 0

match n:
    case n if n < 0:
        print('Number is negative')
    case n if n == 0:
        print('Number is zero')
    case n if n > 0:
        print('Number is positive')
# n = 0
#
# match n:
#     case n < 0:
#         print('Number is negative')
#     case n == 0:
#         print('Number is zero')
#     case n > 0:
#         print('Number is positive')