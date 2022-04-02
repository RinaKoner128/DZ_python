#1
text = "a"
with open('test1.txt', 'w', encoding='utf-8') as f:
    while text != "":
        text = input('Введите данные: ')
        f.writelines(text+'\n')

#2
with open('test1.txt', 'r', encoding='utf-8') as f:
    r = f.readlines()
    count = len(r)
    print('Число строк= ', count)
    for el in r:
        count = el.split()
        print('В этой строке ', len(count), ' слов')

#3
text = "a"
summ=0
with open('test2.txt', 'r', encoding='utf-8') as f:
    """
    Реализация варианта для программной
    записи и выполнения задания
    (но нужно поменять режим файла на 'w+')
    """
    # while text != "":
    #     text = input('Введите данные: ')
    #     f.writelines(text+'\n')
    # f.seek(0)
    r = f.readlines()
    try:
        for el in r:
            count = el.split()
            summ = summ + float(count[1])
            if float(count[1]) < 20000:
                print(f'Сорудник: {count[0]} получает оклад меньше нормы')
    except IndexError:
        print()
    print(f'Средний доход сотрудников составляет: {summ / (len(r) - 1)} рублей')

#4
numbers = {
    'One':'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_list = []
new_list_l = []
with open('test4.txt', 'r', encoding='utf-8') as f:
    r = f.readlines()
    for el in r:
        el = el.split()
        new_list = [numbers[el[0]] if el.index(i) == 0 else i for i in el]
        with open('test4_1.txt', 'a', encoding='utf-8') as f:
            f.seek(0)
            f.writelines(' '.join(new_list)+'\n')

#5
with open('test5.txt', 'w+', encoding='utf-8') as f:
    f.write(input('Введите числа: '))
    f.seek(0)
    r = f.readline().split()
    number_lis = list(map(int, r))
    print(sum(number_lis))

#6
summ=0
teach_list={}
with open('test6.txt', 'r', encoding='utf-8') as f:
    r = f.readlines()
    for el in r:
        for i in el.split():
            for j in i.split('('):
                if j.isdigit():
                    summ =summ + int(j)
        teach_list[el.split()[0]]=summ
        print(teach_list)
        summ = 0

#7
import json

count = 0
cr_profit=0
firm_dict={}
firm_list=[]
average_profit = {}
with open('test7.txt', 'r', encoding='utf-8') as f:
    r = f.readlines()
    for el in r:
        i = el.split()
        profit = float(i[1]) - float(i[2])
        if profit >=0:
            count +=1
            cr_profit = cr_profit + profit
        try:
            firm_dict[el.split()[0]]=profit
            average_profit["average_profit"] = cr_profit/count
        except ZeroDivisionError:
            print()
    firm_list.append(firm_dict)
    firm_list.append(average_profit)
with open("file.json", "w", encoding='utf-8') as write_f:
    json.dump(firm_list, write_f)


