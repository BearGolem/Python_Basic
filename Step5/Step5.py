#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

work_file = open("some_file_S5.txt", 'w')
i = 'a'

while len(i) > 0:
    i = input('Введите текст: ')
    if len(i) > 0:
        work_file.write('{}\n'.format(i.strip()))

work_file.close


#Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

work_file = open("some_file_S5.txt", 'r')

str_count = 0

with open("some_file_S5.txt") as smtxt:
    for line in smtxt:
        str_count += 1
        words_list = line.split(' ')
        print('строка {} содержит {} слова(о)'.format(str_count, len(words_list)))

work_file.close

#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

work_file = open("Emploee_S5.txt", 'r')

str_count = 0
big_money = 0

with open("Emploee_S5.txt") as smtxt:
    for line in smtxt:
        str_count += 1
        words_list = line.split(' ')
        big_money += int(words_list[1])
        if int(words_list[1]) < 20000:
            print('Сотрудник {} влачит жалкое существование на зряплату в {} рублей'.format(words_list[0], words_list[1]))

    print('Средняя зарплата {} рублей'.format(big_money/str_count))

work_file.close

#Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

work_file = open("Countless_S5.txt", 'r')
new_file = open('smthnew_S5.txt', 'w')
vocab_bullary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("Countless_S5.txt") as smtxt:
    for line in smtxt:
        words_list = line.split(' ')
        new_file.write(line.replace(words_list[0], vocab_bullary[words_list[0]]))

work_file.close
new_file.close


#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

new_file = open('Digits_S5.txt', 'w')
some_dig = []
digs_sum = 0

for i in range(random.randint(1, 30)):
    new_file.write('{} '.format(random.randint(1, 100)))

new_file.close

new_file = open('Digits_S5.txt', 'r')

with open('Digits_S5.txt') as digits_sum:
    for line in digits_sum:
        some_dig = line.strip().split()
        for i in some_dig:
            digs_sum += int(i)

print(digs_sum)
new_file.close


#Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

new_file = open('AnyLesson_S5.txt', 'r')

vocab_vocab = {}

with open('AnyLesson_S5.txt') as less_ones:
    for line in less_ones:
        temp_list = line.split(': ')
        vocab_vocab[temp_list[0]] = int(temp_list[1].split(') ')[0][0:len(temp_list[1].split(') ')[0])-2]) + int(temp_list[1].split(') ')[1][0:len(temp_list[1].split(') ')[1])-3]) + int(temp_list[1].split(') ')[2][0:len(temp_list[1].split(') ')[2])-6])

print(vocab_vocab)


#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

more_lists = [{}, {}]
i = 0
some_cash = 0

with open('RosReestr_S5.txt', 'r') as anothe_firm:
    for line in anothe_firm:
        more_lists[0][line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        if int(line.split(' ')[2]) - int(line.split(' ')[3]) > 0:
            i += 1
            some_cash += int(line.split(' ')[2]) - int(line.split(' ')[3])

more_lists[1]['average_profit'] = some_cash/i

with open('RosReestr_S5.json', 'w') as anothe_file:
    json.dump(more_lists, anothe_file)