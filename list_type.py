student = ['Nguyen Van A', 'Nguyen Van B', 'Nguyen Van C']
print("student[0]", student[0])
print("student[1]", student[1])
print("student[2]", student[2])
print("student[-1]", student[-1])
print("student[-2]", student[-2])
print("student[-3]", student[-3])
print("student[0:]", student[0:])
print("student[-1:]", student[-1:])
print("student[-3:2]", student[-3:2])

#Sửa đổi và xóa bỏ giá trị phần tử trong list.
student[0] = "12345"
print("update student[0]", student)
del student[0]
print("delete student[0]", student)
studentA = ["Nguyen Van A", "Mail", 39]
studentB = ["Nguyen Van B", "Femail", 39]
student[0] = studentA
student[-1] = studentB
print('New student[]: ', student)
print('New student[0][0]: ', student[0][0])