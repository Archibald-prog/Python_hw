def int_func(text):
    result = text.title()
    return result


my_string = str(input('Введите строку из маленьких латинских букв через пробелы: '))
print(int_func(my_string))
