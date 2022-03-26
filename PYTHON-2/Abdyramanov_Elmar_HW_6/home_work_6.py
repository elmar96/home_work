import re


class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


files = 'full_name_file.txt'
files1 = 'email_file.txt'
files2 = 'name.txt'
files3 = 'color_file.txt'
file_path4 = 'MOSK_DATE.txt'


def MainFunc():
    file_reader4 = open(file_path4, mode='r', encoding="Latin-1")
    final_results4 = open(files, mode='w', encoding="Latin-1")

    text = file_reader4.read()

    s4 = r'[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+'
    results_all = re.findall(s4, text)

    for item in results_all:
        final_results4.write(item + '\n')
    print(f'Total:{str(len(results_all))}')

    file_reader3 = open(file_path4, mode='r', encoding="UTF-8")
    final_results3 = open(files1, mode='w', encoding="UTF-8")

    text3 = file_reader3.read()

    s3 = r'\w+@\w+.[a-z]+'
    results_all1 = re.findall(s3, text3)

    for item in results_all1:
        final_results3.write(item + '\n')
    print(f'Total:{str(len(results_all))}')

    file_reader2 = open(file_path4, mode='r', encoding="UTF-8")
    final_results2 = open(files3, mode='w', encoding="UTF-8")

    text2 = file_reader2.read()

    s2 = r'#\w+'
    results_all2 = re.findall(s2, text2)

    for item in results_all2:
        final_results2.write(item + '\n')
    print(f'Total:{str(len(results_all))}')

    file_reader1 = open(file_path4, mode='r', encoding="UTF-8")
    final_results1 = open(files2, mode='w', encoding="UTF-8")

    text1 = file_reader1.read()

    s1 = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+\w+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+[0-9]" \
         r"|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+[0-9]"
    results_all3 = re.findall(s1, text1)

    for item in results_all3:
        final_results1.write(item + '\n')
    print(f'Total:{str(len(results_all3))}')


MainFunc()
