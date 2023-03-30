#r, w, a, x
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

# for x in f:
#     print(x)
#
# f.close()
# print(f.readline()) # # error
f = open('demofile2.txt', 'a')
f.write('Now the file has more content!')
f.close()

# open and read the file after the appending:
f = open('demofile2.txt', 'r')
print(f.read())

f = open('demofile3.txt', 'w')
f.write('Whoops! I have deleted the content!')
f.close()

# open and read the file after the appending:
f = open('demofile3.txt', 'r')
print(f.read())