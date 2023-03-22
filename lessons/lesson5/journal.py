# Declaring datas
register = []
student = {}

# Read data from user
st_num = int(input('Enter how many students there are' + '\n'))
sub_num = int(input('Enter how many subjects there are' + '\n'))
for j in range(0,st_num):
    s_name = input('Name\n')
    student.update({"Name": s_name})
    for i in range(0, sub_num):
        subject = input('Subject\n')
        mark = int(input('Mark\n'))
        student.update({subject: mark})
    register.append(student.copy())
print(student)
register[0].update({'age': 18})
print(student)
print(register)
