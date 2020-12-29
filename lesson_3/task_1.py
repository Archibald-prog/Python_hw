def division():
    num_1 = int(input('Enter a number: '))
    num_2 = int(input('Enter a number: '))
    try:
        return num_1 / num_2
    except ZeroDivisionError:
         print('Incorrect data. Zero division')


print(division())
