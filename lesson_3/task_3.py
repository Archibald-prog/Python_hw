def my_func(num_1, num_2, num_3):
    list_1 = [num_1, num_2, num_3]
    list_2 = []
    i = 0
    while i <= 1:
        max_n = max(list_1)
        list_2.append(max_n)
        list_1.remove(max_n)
        i += 1
    my_sum = sum(list_2)
    return my_sum


print(my_func(40, 20, 30))