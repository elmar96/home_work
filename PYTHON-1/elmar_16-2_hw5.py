movies = {
    "Django_Unchained": {"John": 10, "Jack": 9},
    "Акыркы_Сабак": {}
}


def add_movie(movie):
    if movie in movies.keys():
        print("НЕТ такого фильма!!!")
    else:
        movies.update({movie: dict()})


def show():
    for name, rates in movies.items():
        print(f"\nФильм: {name}")
        if len(rates) == 0:
            print("НЕТ рейтинга!!!")
        else:
            print("Рейтинг:")
            for user, rate in rates.items():
                print(f"{user}:{rate}")


def add_rete(movie):
    if movie not in movies.keys():
        print("НЕТ такого фильма!!!")
    else:
        name = input("Введите своё имя:").capitalize()
        rate = int(input("Введите рейтинг: "))
        if rate < 0 or rate > 10:
            print("Рейтинг только от 1 до 10!")
        elif name in list(movies[movie].keys()):
            print("такой имя уже есть!!")
        else:
            movies[movie].update({name: rate})
            print(f"Добавлен рейтинг для Interstellar: {name} оценил его {rate}")


def rate_view():
    for movie, rate in movies.items():
        if len(rate) == 0:
            print(f"У этого фильма {movie} нет рейтинга !!!")
        else:
            rates_list = list(rate.values())
            average = round(sum(rates_list) / len(rates_list), 1)
            print(f"фильм:{movie} - рейтинг: {average}")


while True:
    show()
    command = int(input("\nВведите команды:"
                        "\n1-добавление фильма "
                        "\n2-добавление рейтинга "
                        "\n3-список рейтингов "
                        "\n0-программа завершена!!!\n"))
    if command == 0:
        print("программа завершена!!!")
        break
    elif command == 1:
        movie = input("Введите название фильма:").capitalize()
        add_movie(movie)
    elif command == 2:
        movie = input("Введите название фильм для добавления рейтинга:").capitalize()
        add_rete(movie)
    elif command == 3:
        rate_view()
    else:
        print("НЕТ такого команды!!!")
