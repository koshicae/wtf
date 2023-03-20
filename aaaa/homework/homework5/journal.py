# Declaring datas
register = []
student = {}

# Read data from user
st_num = int(input('Enter how many students there are'))
sub_num = int(input('Enter how many subjects there are'))
for j in range(0,st_num):
    s_name = input('Name')
    student.update({"Name": s_name})
    for i in range(0, sub_num):
        subject = input('Subject')
        mark = int(input('Mark:'))
        student.update({subject: mark})
    register.append(student)
print(register)