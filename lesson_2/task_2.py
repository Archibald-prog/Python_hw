n = int(input('Введите число элементов списка: '))
my_list = []
i = 0
while i < n:
    my_list.append(input('Введите элемент списка: '))
    i += 1
print(my_list)

if n % 2 != 0:
    last_el = my_list.pop()
    n = n - 1

my_list_2 = []
i = 0
var_count = 0

while var_count < n/2:
    var_1, var_2 = my_list[i], my_list[i + 1]
    var_1, var_2 = var_2, var_1
    new_element = var_1, var_2
    my_list_2.append(new_element)
    i += 2
    var_count += 1

try:
    my_list_2.append(last_el)
except NameError:
    print('В списке четное число элементов')

my_list_3 = []
for i in my_list_2:
    if type(i) == tuple:
        for j in i:
            my_list_3.append(j)
    else:
        my_list_3.append(i)

print(my_list_3)
