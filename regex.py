import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

f = "phonebook_raw.csv"
pattern_phone = r"(\+?\d{1})\s*(\(?)(\d{3})(\)?)(\s*|-*)(\d{3})(-*)(\d{2})(-*)(\d{2})"
pattern_add_phone = r"доб.\s*(\d{4})"
substitution = r"+7(\3)\6-\8-\10"
sub_add_phone = r"доб.\1"


def right_phone(person_list, pattern_ph, pattern_add_ph, sub_ph, sub_add_ph):
    '''
    функция, которая определяет телефонные номера
    и возвращает их в требуемой форме
    '''
    add_phone_correct = ''
    phone_correct = ''
    raw_phone = person_list[5]
    if re.search(pattern_ph, raw_phone) is not None:
        phone = re.search(pattern_ph, raw_phone).group()
        phone_correct = re.sub(pattern_ph, sub_ph, phone)
        if re.search(pattern_add_ph, raw_phone) is not None:
            add_phone = re.search(pattern_add_ph, raw_phone).group()
            add_phone_correct = re.sub(pattern_add_ph, sub_add_ph, add_phone)
    if phone_correct:
        phone = phone_correct + ' ' + add_phone_correct
        return phone


def file_opener(file):
    with open(file, encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def phonebook(file_name, pattern_ph, pattern_add_ph, sub_ph, sub_add_ph):
    '''
    Функция, которая создает список номеров с корректными именами
    и телефонами. Также в функции производится проверка дублирования
    записей в телефонной книге
    '''
    raw_contact_list = file_opener(file_name)
    phonebook_list = []
    check_list = []
    for person in raw_contact_list:
        correct_list = []
        phone = right_phone(person, pattern_ph, pattern_add_ph, sub_ph, sub_add_ph)
        name = (person[0] + ' ' + person[1] + ' ' + person[2]).rstrip()
        check_name_list = name.split()
        check_name = check_name_list[0] + ' ' + check_name_list[1]
        if check_name not in check_list:
            check_list.append(check_name)
            correct_list.append(name)
            correct_list.append(phone)
            phonebook_list.append(correct_list)
    return phonebook_list

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
# names = []
# phonebook_list = []


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def writer_file():
    with open("phonebook.csv", "w") as file:
      datawriter = csv.writer(file, delimiter=',')
      # Вместо contacts_list подставьте свой список
      datawriter.writerows(phonebook(f, pattern_phone, pattern_add_phone, substitution, sub_add_phone))


if __name__ == '__main__':
    pprint(phonebook(f, pattern_phone, pattern_add_phone, substitution, sub_add_phone))
    writer_file()
