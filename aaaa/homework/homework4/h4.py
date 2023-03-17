print('Угадай название животного:')
a = str(input())
b = "cat"
while a != b:
    print("попробуй другое")
    a = str(input())
print("ты отгадал котика молодес!!!")