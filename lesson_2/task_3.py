month_list = [0, 'зима', 1, 'зима', 2, 'зима',
              3, 'весна', 4, 'весна', 5, 'весна',
              6, 'лето', 7, 'лето', 8, 'лето',
              9, 'осень', 10, 'осень', 11, 'осень']
month_number = int(input('Введите номер месяца: '))
if month_number == 12:
    month_number = 0

print(month_list[month_number*2 + 1])

month_list_dict = {1: 'зима', 2: 'зима',
                   3: 'весна', 4: 'весна', 5: 'весна',
                   6: 'лето', 7: 'лето', 8: 'лето',
                   9: 'осень', 10: 'осень', 11: 'осень',
                   12: 'зима'}

month_number = int(input('Введите номер месяца: '))

print(month_list_dict.get(month_number))

