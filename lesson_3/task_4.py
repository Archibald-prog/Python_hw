def my_func(x, y):
    power = x**y
    return power

# решение с циклом
#     power = x
#     i = 2
#     while True:
#         power = power*x
#         i += 1
#         if i > abs(y):
#             break
#     result = 1/power
#     return result


while True:
    num_1 = float(input('Введите положительное число: '))
    if num_1 > 0:
        break
while True:
    num_2 = int(input('Введите целое отрицательное число: '))
    if num_2 < 0:
        break

print(my_func(num_1, num_2))