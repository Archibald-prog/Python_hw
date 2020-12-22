user_number = input('Enter a positive integer: ')
total_number = []
i = 0

while i < len(user_number):
    total_number.append(user_number[i])
    i += 1
total_number = [int(x) for x in total_number]

max_number = total_number[0]
i = 1
while i < len(total_number):
    if max_number < total_number[i]:
        max_number = total_number[i]
    i += 1
print('The biggest number in {} is {}.' .format(user_number, max_number))
