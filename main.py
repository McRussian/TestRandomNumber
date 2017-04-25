__author__ = 'McRussian Andrey'

import random
import math
import pylab

def getRandomFromInreval(a, b, x, val, eps):
    '''
    Функция возвращает случаное число, равномерно распределенное в интервале от a до b.
    если значение x лежит в этом диапазоне,
    к значение val прибавляется равномерно распределенная ошибка от -eps до eps,
    иначе возвращается 0
    '''
    if x <=b and x >= a:
        return val + random.uniform(-eps, eps)
    else:
        return 0



def getRandomGauss(mu, delta, x, eps):
    '''
    Функция возвращает значение функции нормального распределения в точке x с некоторой погрешностью eps
    Функция нормального распределения характеризуется двумя параметрами mu, delta

    '''
    f = math.exp(-(x - mu)**2/(2 * delta**2)) / (delta * math.sqrt(2 * math.pi))
    return f + random.uniform(-eps, eps)



#Исходные данные, количество точек, интервал распределения, кол-во функций распределения
N = 200
a = 0
b = 10
h = (b - a) / N

eps =0.005

count_gauss = 5
count_random = 2

#ЗДесь будут храниться все нормальные распределения и равномерные распределения
gauss_list = []
random_list = []

#список значений параметров для нормального арспределения
list_mu = [m / 2 for m in range(a, 2 * b)]
list_delta = [m / 2 for m in range(a, 2 * b)]

#Генерим заданное количество нормальных распределений
#Случайно выбирается параметры mu, delta из соответсвующих списков
#Полученная пара значений в виде кортежа записывается в список нормальных распределений
for i in range(count_gauss):
    mu = random.choice(list_mu)
    delta = random.choice(list_delta)
    gauss_list.append((mu, delta))

#Генерим заданное количество равномерных распределений
#Случайно генерим диапазон для равномерного рапсределения, и значение медианы...
#ПОлученная тройка значений в виде кортежа записывается в список равномерных распределений
for i in range(count_random):
    left = random.randint(a, (b - a) / 2)
    right = random.randint(left, b)
    value = random.uniform(0, 0.2)
    random_list.append((left, right, value))

print(gauss_list)
print(random_list)


#Строим тестовую последовательность данных
x = []
y = []
for i in range(N):
    #Перемнная x равномерно распределена по заданному диапазону
    xt = i * h
    yt = 0
    #В соответствующую переменную y добавляем вклад всех нормальных арспределений
    for k in range(count_gauss):
        yt = yt + getRandomGauss(gauss_list[k][0], gauss_list[k][1], xt, eps)
    #к переменной y добавляем вклад всех равномерных распределений
    for k in range(count_random):
        yt = yt + getRandomFromInreval(random_list[k][0], random_list[k][1], xt, random_list[k][2], eps)
    #Запоминаем пару (x, y) в разных списках
    x.append(xt)
    y.append(yt)

#Выводим результат в виде графика
pylab.plot(x, y)
pylab.show()

