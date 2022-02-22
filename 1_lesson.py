#Задание 1
print('Переводим типы')
p_int = int(input('Введите целое число: '))
p_float = float(input('Введите число с плавающей точкой: '))
p_str = str(input('Введите текст: '))
p_bool = bool(input('Введите False или True: '))
print(p_int, 'имеет тип: ', type(p_int))
print(p_float, 'имеет тип: ', type(p_float))
print(p_str, 'имеет тип: ', type(p_str))
print(p_bool, 'имеет тип: ', type(p_bool))

#Задание 2
print('Правильный секундомер')
time = int(input('Введите время в секундах: '))
hours= str(time // 3600)
minute = str(time%3600//60)
seconds =str(time%3600%60)
if int(hours)<10:
    hours="0"+hours
if int(minute)<10:
    minute="0"+minute
if int(seconds)<10:
    seconds="0"+seconds
print('{}:{}:{}'.format(hours,minute,seconds))


#Задание 3
print('Сложение числа')
number = input('Введите число: ')
one_number = number
two_number = number+number
tree_number = number+number+number
result = int(one_number)+ int(two_number)+ int(tree_number)
print(result)


#Задание 4
print('Ищем максимальную цифру  числе')
number = int(input('Введите целое положительное число: '))
result = 0
while number > 0:
    n1 = number % 10
    n2 = number % 100 // 10
    if result < n1 or result < n2:
        if n1 >= n2:
            result = n1
        else:
            result = n2
    number = number//100
print(result)


#Задание 5-6
print('Задача прибыльности фирмы')
revenue = float(input('Введите Вашу выручку: '))
cost = float(input('Введите Ваши издержки: '))
if revenue > cost:
    print('Вы работаете на прибыль')
    rent = revenue / cost *100
    print('Рентабельность всей фирмы составляет: ',rent, '%')
    count = int(input('Введите количество сотрудников фирмы: '))
    revenue_people = revenue / count
    print('Прибыль фирмы в расчёте на одного сотрудника составляет', revenue_people)
elif revenue < cost:
    print('Вы работаете в убыток')
else:
    print('Вы работаете в "0"')


#Задание 6(7)
print('Расписание спортсмена')
start = float(input('Введите начальную цель: '))
finish = float(input('Введите конечную цель: '))
day = 1

while start < finish:
    start = start+start*0.1
    day+=1
print('Спортсмен достиг результата на', day ,'день')