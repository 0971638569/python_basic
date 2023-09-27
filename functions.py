c = 0
result = 0
def sum(*number):
    global result
    for i in number:
        result += int(i)
    return result
sum(1,2,'3')
print(result)

#lambda function(anonymous function - hàm ẩn danh)
lambdaF = lambda a,b: a + b

print(lambdaF(1,2))