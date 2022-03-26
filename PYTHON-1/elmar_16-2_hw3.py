import a

mentor = ['Эсенбек', 'Мирхад', 'Беки']
while True:
    if len(mentor) <= 5:

        command = input(
            f'{mentor}\n'
            f'Выберите команду: \n '
            f'1 - добавление \n '
            f'2 - изменение \n '
            f'3 - удаление \n '
            f'4 - выход \n:')
        if command == '4':
            print(tuple(mentor))
            break
        if command == '1':
            new_mentor = input('\nВведи имя ментора, которого вы хотите добавить: ').capitalize()
            if new_mentor in mentor:
                print("этот ментор уже есть в списке")
            elif len(new_mentor) <= 15:
                mentor.append(new_mentor)
            else:
                print('\n Имя должно содержать не более 15 букв')
                continue

        if command == '2':
            changed_mentor = input('\n Введи имя ментора, ты хочешь заменить: ').capitalize()
            added_mentor = input('\n Введи имя нового ментора:').capitalize()
            if changed_mentor in mentor and len(added_mentor) <= 15:
                mentor.remove(changed_mentor)
                mentor.append(added_mentor)
            elif changed_mentor in mentor and len(added_mentor) != 15:
                print('\n Имя должно содержать не более 15 букв')
                continue
            else:
                print('\n Ментора, которого вы хотите изменить, нет в списке')
                continue

        if a == "3":
            continue
        b = input('Выберите способ по которому будет удалять i|n:')
        if b == 'n':
            g = input('ведите имя').capitalize()
            if g in mentor:
                mentor.remove(g)
            else:
                print("этого ментора нет в списке")

        elif b == 'i':
            f = int(input('введите индекс'))
            if f > len(mentor) - 1:
                print('такого индекс нет')
                continue
            else:
                del mentor[f]

    else:
        print(' \n список не имеет быть больше 5 менторов \n')
        break


