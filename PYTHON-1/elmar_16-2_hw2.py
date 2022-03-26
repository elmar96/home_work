name = input("Введите слово: ")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
          "abcdefghijklmnopqrstuvwxyz" \
          "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
          "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
vowels = "AEIOUYaeiouy" \
         "АОУЭЫЯЁЕЮИаоуэыяёеюи"
consonants = "BCDFGHJKLMNPQRSTVWXZ" \
             "bcdfghjklmnpqrstvwxz" \
             "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ" \
             "бвгджзйклмнпрстфхцчшщ"
s1 = 0
for letter in name:
    if letter in letters:
        s1 += 1
print(f'Количество букв: {s1}')
s2: int = 0
for letter in name:
    if letter in vowels:
        s2 += 1
print(f'Глассных букв: {s2}')

s3 = 0
for letter in name:
    if letter in consonants:
        s3 += 1
print(f'Соглассных букв: {s3}')

percent1 = s2 / s1 * 100
percent2 = s3 / s1 * 100
# percent2 = s3 * 100 / 10
print(f"Гласные/Согласные:{percent1:.2f}%/{percent2:.2f}%")
