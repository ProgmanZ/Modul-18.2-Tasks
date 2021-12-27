# Задача 3. IP-адрес

print('Программа ввода IP адреса.')

ip_address = []
count = 1
while True:

    group = int(input(f'Введите {count} группу цифр IP адреса: '))
    if 0 <= group < 255 and (count == 2 or count == 3):
        ip_address.append(group)
    elif 0 < group < 255 and (count == 1 or count == 4):
        ip_address.append(group)
    elif count == 1 or 4:
        print(f'{group}группа цифр должна быть больше 0 и меньше 255.')
        continue
    else:
        print('Непредвиденное событие.')
    count += 1
    if count == 5:
        break

print("Вы ввели следующий IP адрес: {first}.{second}.{third}.{fourth}.".format(
        first=ip_address[0],
        second=ip_address[1],
        third=ip_address[2],
        fourth=ip_address[3]
))
