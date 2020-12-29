def personal_data(data_dict):
    data_dict['user name'] = input('Enter your name: ')
    data_dict['user surname'] = input('Enter your surname: ')
    data_dict['user year of birth'] = input('Enter your year of birth: ')
    data_dict['user city of residence'] = input('Enter city of residence: ')
    data_dict['user email'] = input('Enter your email: ')
    data_dict['user phone number'] = input('Enter your phone number: ')
    result = " ".join(f"{key} - {val};" for key, val in data_dict.items())
    print(result)


user_data = {'user name': '',
             'user surname': '',
             'user year of birth': '',
             'user city of residence': '',
             'user email': '',
             'user phone number': ''}


personal_data(user_data)