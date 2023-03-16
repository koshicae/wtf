a = int(input())
b = 5
# a = 2
# b = int(input())
# while a != b:
#     print("попробуй другое")
#     a = int(input())
while a != b:
    if a > b:
        print("вариант слиш")
    else:
        print("вариант слишком мала, попр еще раз")
    b = int(input("введите свой номер"))

print("ты угадал число молодес!!!")