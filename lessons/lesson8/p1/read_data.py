import json


def read_dataa():
    f = open('student_data.txt', 'r')
    print(f.read())
    f.close()