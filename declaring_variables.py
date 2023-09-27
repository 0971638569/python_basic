# tenBien là tên của biến mà các bạn muốn đặt.
# Tên biến này không được bắt đầu bằng số hay các ký tự đặc biệt, mà chỉ được bắt đầu bằng chữ cái hoặc ký tự _ và nó có phân biệt hoa thường.
# giaTrilà giá trị của biến mà bạn muốn gán.
name = "Nguyen Van Phuc"
a = b = c = 0
firstName, age, male = "Nguyen Van Phuc", 30, True
pfloat = 6.9
plist = [1,2,3, '4', '5', pfloat]
ptulip = (1, '2', True)
pdictionary = {a, name, True, pfloat}

print("variables: name = ", name)
print("variables: a, b, c = ", a,b,c)
print("variables: firstName, age, male = ", firstName, age, male)

#Các kiểu dữ liệu trong Python.
print("string: ", firstName) #string
print("interger: ", age) #interger
print("float: ", pfloat) #float
print("list: ", plist) #list
print("tulip: ", ptulip) #tulip
print("dictionary: ", pdictionary) #dictionary

#Kiểm tra kiểu dữ liệu
print("Check data type list: ", type(list))
print("Check data type dictionary: ", type(pdictionary))

#Chuyển đổi kiểu dữ liệu
print("data type conversion float: ", float(age))
print("data type conversion int: ", int('6'))
print("data type conversion str: ", int(age))
print("data type conversion complex: ", complex(pfloat))
print("data type conversion tuple: ", tuple(plist), tuple(pdictionary))
print("data type conversion dictionary: ", dict({"key1": 1, "key2": 2, "keyN": 3}))
print("data type conversion hex: ", hex(age))
print("data type conversion oct: ", oct(age))

#Thay đổi ngắt dòng print.
print(name, end = '-')
print(age, "year old")
