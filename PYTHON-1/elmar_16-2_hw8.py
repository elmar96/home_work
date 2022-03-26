import datetime
from random import randint


def get_count_attempts() -> int:
    attempts_count = None
    while True:
        try:
            attempts_count = int(input('Сколько попыток? '))
            break
        except ValueError:
            print('Количество попыток должен быть только числом!')
            continue
    return attempts_count


def get_user_name() -> str:
    return input('Укажите имя? ')


numbers_of_attempts = get_count_attempts()
user_name = get_user_name()
iterations = numbers_of_attempts

with open('results.txt', 'w+') as result_file:
    start = datetime.datetime.now()
    while True:
        if iterations <= 0:
            result_file.write(f'было {numbers_of_attempts} попыток,'
                              f' потраченное время: {datetime.datetime.now() - start} '
                              f' имя:{user_name}\n ')
            break
        first_number, second_number = (randint(1, 9) for _ in range(2))
        user_result = int(input(f'{first_number} * {second_number} = ? '))
        correct_result = first_number * second_number
        print(correct_result)
        result_file.write(f'{first_number} * {second_number} = {user_result} ({correct_result}) '
                          f'{"правильно" if user_result == correct_result else "неправильно"}\n')
        iterations -= 1
