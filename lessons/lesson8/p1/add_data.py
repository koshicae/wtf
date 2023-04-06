import student


def add_dataa():
    a = student.student_register()
    f = open('student_data.txt', 'w')
    f.write(str(a))
    f.close()

def edit_dataa():
    f = open('student_data.txt', 'rw')
    f.read()
    f.close()
