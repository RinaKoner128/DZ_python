#1
def dele(a, b):
    try:
        print(a/b)
    except:
        print('На ноль делить нелья')

dele(int(input('Введите делимое: ')), int(input('Введите делитель: ')))


#2
def user_info(name, famile, age, sity, email, phone):
    print('Имя: {},'
          ' Фамилия: {},'
          ' Год рождения: {}, '
          ' Город рождения: {},'
          ' Email: {},'
          ' Номер телефона: {}'
          .format(name, famile, age, sity, email, phone))

name=input('Введите Имя: ')
famile=input('Введите Фамилию: ')
age=input('Введите год рождения: ')
sity=input('Введите город рождения: ')
email=input('Введите Email: ')
phone=input('Введите номер телефона: ')
user_info(name, famile, age, sity, email, phone)


#3
def my_func(a, b, c):
    user_list=[]
    user_list.append(a)
    user_list.append(b)
    user_list.append(c)
    user_list.sort()
    return user_list[1]+user_list[2]
try:
    print(my_func(int(input('Первое число: ')), int(input('Второе число: ')), int(input('Третье число: '))))
except ValueError:
    print('Цифры надо вводить по одному')


#4
def my_func(x, y):
    res = 1
    for i in range(1, abs(y)+1):
        res =res*1/x
    return res

print(my_func(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))


#5
def summa():
    res_summ=0
    while True:
        number_lis = input().split()
        number_lis = list(map(int, number_lis))
        for number in number_lis:
            if number == 0:
                print(res_summ)
                return
            else:
                res_summ=res_summ+number
        print(res_summ)

summa()


#6-7
def int_func(text):
    text=text.title()
    return text

print(int_func(input('Введите слова из маленьких латинских букв: ')))


