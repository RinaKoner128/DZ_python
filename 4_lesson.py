import sys
from functools import reduce
from itertools import count, cycle
from math import factorial

#1
try:
    print("Зарплата состовляет",(int(sys.argv[1])*int(sys.argv[2]))+int(sys.argv[3]), "рублей")
except IndexError:
    print('Необходимо ввести 3 числовых параметра')

#2
old_list=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list=[old_list[el] for el in range(1,len(old_list)) if old_list[el] > old_list[el-1]]
print(new_list)


#3
zwie_list=[el for el in range(20,240) if el % 20 == 0 or el % 21 == 0]
print(zwie_list)


#4
old_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list=[el for el in old_list if old_list.count(el)<2]
print(new_list)


#5
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, [el for el in range(100,1001) if el % 2 == 0]))


#6
с = 0
progr_lang = ["python", "java", "perl", "javascript"]
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

for el in cycle(progr_lang):
    if с > 6:
        break
    print(el)
    с += 1


#7
n=7
def fact(n):
    for el in (factorial(i) for i in range(0, n)):
        yield el

for el in fact(n):
    print(el)