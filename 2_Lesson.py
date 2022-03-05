#Первное задание
print('Первное задание')
print('*'*50)
user_list = [1, 735.5, 'Hello']
for i in user_list:
    print(i, ' - ', type(i))


#Второе задание
print('Второе задание')
print('*'*50)
new_list=[]
result=[]
user_list =input('Введите эелементы через запятую: ').split(',')
for i in range(len(user_list)):
    try:
        if i%2==0:
            reserv=user_list[i]
            user_list[i]=user_list[i+1]
            user_list[i+1] = reserv
    except IndexError:
        user_list[i]
print(user_list)


#Третье задание
print('Третье задание')
print('*'*50)
time = {"Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11], "Зима": [12, 1, 2]}
month=int(input('Введите номер месяца: '))
for el in time:
    if month in time[el]:
        print(el)
        break

#Четвертое задание
print('Четвертое задание')
print('*'*50)
element=''
uset_str=input('Введите слова через пробел: ').split()
for i in uset_str:
    if len(i) > 10:
        element = i[:10]
        uset_str.insert(uset_str.index(i)+1, element)
        uset_str.pop(uset_str.index(i))
for ind, el in enumerate(uset_str):
    print(ind+1, el)


#Пятое задание
print('Пятое задание')
print('*'*50)
my_list = [7, 5, 3, 3, 2]
number=int(input('Введите цифру: '))
my_list.append(number)
my_list.sort()
my_list.reverse()
print(my_list)


#Шестое задание
print('Шестое задание')
print('*'*50)
catalog=[]
num=1

while input('Добавить товар?').lower()=='да':
    name=input('Введите название товара: ')
    price=input('Введите стоимость товара: ')
    count=input('Введите количество товара: ')
    es=input('Введите еденицу измерения товара: ')
    product = {'Наименование': name, 'Цена': price, 'Количество': count, 'ед': es}
    ctg = (num, product)
    catalog.append(ctg)
    num += 1
print(*catalog, sep="\n")