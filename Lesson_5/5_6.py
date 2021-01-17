"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
dict_lessons = {}
def numer_in_string(st):
    l = ''
    for i in st:
        if i.isdigit():
            l += i
        else:
            l += ' '
    return l.split()

with open('lesson_5_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        number_h = 0
        for i in numer_in_string(line):
            number_h += int(i)
        dict_lessons[line.split()[0]] = number_h
print(dict_lessons)
