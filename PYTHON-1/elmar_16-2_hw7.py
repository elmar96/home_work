import datetime
from random import randint

start = datetime.datetime.now()
number = randint(0, 100)
c = 0
attemp = 0
while 1:
    try:
        user_num = int(input('Введи число до 100:'))
    except TypeError:
        print('Oops!  That was no valid number.  Try again...')
        continue
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        continue
    else:
        if 0 <= user_num <= 100:
            attemp += 1
            if user_num == number:
                print(f"Количество попыток:{attemp}")
                wasted_time = datetime.datetime.now() - start
                print(f'потрачена времени: {wasted_time}')
                break
            elif user_num < number:
                print(f'Число >{user_num}\n')
            elif user_num > number:
                print(f'Число <{user_num}\n')
        else:
            print(f"Введите целое число от {0} до {100}")
