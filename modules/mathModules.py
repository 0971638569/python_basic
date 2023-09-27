class ExceptionsModule(Exception):
    def __init__(self, value):
        print('Error: ', value)

def sum(*number):
    result = 0
    for i in number:
        result += int(i)
    return result

def sub(*number):
    result = 0
    for i in number:
        result -= int(i)
    return result

def mul(*number):
    result = 1
    for i in number:
        # if(i == 0):
            # raise ExceptionsModule('111111111')
        result *= int(i)
    return result

def div(*number):
    result = 1
    for i in number:
        result /= int(i)
    return result