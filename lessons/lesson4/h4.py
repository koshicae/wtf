print('угадай название животного:')
a = str(input()).lower()
b = "кот"
while a != b:
    print("попробуй другое")
    a = str(input()).lower()
print("ты отгадал котика молодес!!!")