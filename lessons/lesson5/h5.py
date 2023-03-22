# Declaring datas
#shift+tab = sdvig (shift) :)
register = []
student = {}

# Read data from user
s_name = input('Name: ')
student.update({"Name": s_name})
mark_sum = 0
for i in range(0, 4):
    subject = input('Subject: ')
    mark = int(input('Mark: '))
    student.update({subject: mark})
    mark_sum += mark
x = str(mark_sum/4)
print(s_name + '\'s average mark is: ' + x)
register.append(student)
print(register)

# avg = sum(student.get(subject) / len(i)
# print("Средний балл: ", avg)
