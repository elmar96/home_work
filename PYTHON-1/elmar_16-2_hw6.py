# 1 - сгенерировать список
ten = [i for i in range(1, 11)]
# 2 - список evens
evens_numbers = list(filter(lambda x: (x % 2 == 0), ten))
# 3 - возведение в квадрат
up = list(map(lambda x: x ** 2, evens_numbers))
print(up)


# 4 - Вывод обьекта по индексу
def get_obj(num_list=tuple(ten)):
    print(f'Список: {ten}\n'
          f'1 - Поиск по индексу\n'
          f'0 - Выход\n')
    command = None
    while command != 0:
        try:
            command = int(input('Выберите команду:'))
            if command == 1:
                try:
                    idx = int(input('Введите индекс:'))
                    print(f'Под индексом: {idx} находится '
                          f'обьект: {num_list[idx]}')
                except IndexError:
                    print(f'Введите индекс от 0 до '
                          f'{len(num_list) - 1}')
        except ValueError:
            print(f'Нужно ввести число(индекс)!')


get_obj()
