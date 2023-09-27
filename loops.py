variables = "123456789"
for variable in variables:
    print(variable)

print("------------------------------")
for i in range(0, 10):
    for j in range(i, 10):
        print(j, end = " ")
    print(" ")

print("------------------------------")
i = 0
while (i < 10):
    j = i
    while (j < 10):
        print(j, end = " ")
        j += 1
    print("")
    i += 1

print("-------------break-----------------")
for i in range(0, 10):
    for j in range(i, 10):
        if (j == 5):
            break
        print(j, end = " ")
    print(" ")

print("-------------continue-----------------")
for i in range(0, 10):
    for j in range(i, 10):
        if (j == 5):
            continue
        print(j, end = " ")
    print(" ")