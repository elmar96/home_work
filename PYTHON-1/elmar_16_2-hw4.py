GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
# 1-Удаление
del GeekTech["bag"]

# 2-Изменение
GeekTech["address"] = "Ибраимова 103"

# 3-добавление
GeekTech.update({"phone number": "+996 770 00 46 30", "instagram": "geektech_kg"})

# 4- Расширение курсов
k = ["UX/UI-дизайнер", "IOS-разработчик"]
GeekTech['courses'].extend(k)
GeekTech['courses'] = tuple(GeekTech['courses'])
# list = tuple(GeekTech)

# 5-“ключ: значение”
for k, v in GeekTech.items():
    print(f"{k} : {v}")

