user_string = str(input('Введите строку из нескольких слов, разделенных пробелами: '))

user_list = user_string.split()

for item in user_list:
    if len(item) > 10:
        num = user_list.index(item)
        short = item[:10]
        user_list.pop(num)
        user_list.insert(num, short)

for item, val in enumerate(user_list, 1):
    print(item, val)
