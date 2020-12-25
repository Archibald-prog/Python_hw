my_list = [7, 5, 3, 2, 1, 4, 8, 9, 6]
print(my_list)
i = 1
user_list = []

while i < 9:
    rating_num = int(input('Введите любое число из списка: '))
    if rating_num in user_list:
        num = user_list.index(rating_num)
        user_list.insert(num - 1, rating_num)
    else:
        user_list.append(rating_num)
    final_list = sorted(user_list, reverse=True)
    print(final_list)
    i += 1