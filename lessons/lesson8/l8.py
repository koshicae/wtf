# удаление файла
import os
#
# try:
#     os.remove('demofile.txt')
# except:
#     print('No such file has been found')

if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('The file does not exist')

#r, w, a, x (создать, создает файл и выдает ошибку если уже создан)
# f = open('demofile.txt')
# print(f.read())

# print('Only 5')
# f = open('demofile.txt', 'r') # режим
# print(f.read(5))
#
# print('Lines')
# print(f.readline())
# print(f.readline())
#
# print('line by line')
#
# for x in f: # # doesn't work
#     print(x)
#
# f.close()
# print(f.readline()) # # error
# f = open('demofile2.txt', 'a')
# f.write('Now the file has more content!')
# f.close()
#
# # open and read the file after the appending:
# f = open('demofile2.txt', 'r')
# print(f.read())
#
# f = open('student_data.txt', 'w')
# f.write('Whoops! I have deleted the content!')
# f.close()
#
# # open and read the file after the appending:
# f = open('student_data.txt', 'r')
# print(f.read())

# import - библиотека, модуль, набор функций

