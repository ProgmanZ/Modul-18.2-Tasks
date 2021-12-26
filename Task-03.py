# Задача 3. IP-адрес

print('Программа ввода IP адреса.')

ip_address = []
count = 1
while True:
    group = int(input(f'Введите {count} группу цифр IP адреса'))
    if 0 < group < 255 and count == 2 or 4:
        ip_address.append(group)
    elif 0 <= group < 255 and count != 1 or 4:
        ip_address.append(group)
    elif count == 1 or 4:
        print(f'{group}группа цифр должна быть больше 0 и меньше 255.')
        continue
    else:
        print('Непредвиденное событие.')
    count += 1
    if count == 4:
        break
print(ip_address)


