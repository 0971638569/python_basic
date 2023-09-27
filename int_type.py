#Nếu như bạn muốn giải phóng một vùng nhớ cho một biến trong Python thì bạn có thể sử dụng lệnh del
age = 30
print("age: ", age)

#Giải phóng một vùng nhớ 
del age
try:
    print("Not Frees a memory area: ", age)
except:
    print("Frees a memory area: ")