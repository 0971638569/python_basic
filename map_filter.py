def mutiply(x):
    return x * x

result = map(mutiply, [1, 2, 3, 4])
result2 = map(lambda x: x * x, [1, 2, 3, 4])
result3 = map(lambda x, y: x + y, ['1', '2'], ['3', '4'])
result4 = filter(lambda x: x % 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])

print(list(result)) # [1, 4, 9, 16]
print(list(result2)) # [1, 4, 9, 16]
print(list(result3))
print(list(result4))  # [1, 3, 5, 7, 9]