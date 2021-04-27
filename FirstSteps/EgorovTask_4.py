# Функции trunc, floor, ceil.
# Функция trunc выполняет отсечение дробной части и оставляет только целую часть числа
# Функция floor выполняет округление вниз до ближайшего целого числа
# Функция ceil выполняет округление вверх до ближайшего целого числа
# для вызова этих вункций нужно выпослнить следующее
# from math import *    # в этом случае просто вызываем функцию
# import math as m    # тогда не надо писать каждый раз math.<функция>, а достаточно m.<функция>
# ''' например''' x = m.ceil(4.5)
import math as m
x = m.ceil(4.5)
# from math import *    # в этом случае просто вызываем функцию
# x = ceil(4.5)
# from math import ceil, sqrt    # из модуля math были вызваны функции округления вверх и квадратного корня
# x = sqrt(ceil(3.4))

# Портос хочет украсить золотым шитьем свою перевязь. Он знает, что один сантиметр золотого шитья стоит один луидор.
# Портосу надо вышить N миллиметров перевязи.
# Причем мастер никогда не возьмется за работу,если ему заплатят меньше,чем стоит работа.Исдачу мастер никогда не отдает
# Какое минимальное количество луидоров Портос должен заплатить мастеру за работу
# Входные данные
# Программе на вход поступает натуральное число N (N ≤ 109) – длина перевязи в миллиметрах.
# Выходные данные
# Выведите на экран минимальное количество луидоров, которые Портос должен отдать за работу.
import math as m
n = int(input())
s = n / 10
print(m.ceil(s))
# После вечеринки компания из N человек хочет добраться домой с помощью такси.
# Максимальное количество человек, которое может уместиться в машину равно 4.
# Сколько машин придется вызвать ребятам, чтобы все могли уехать?
# Программа получает на вход положительное целое число N - количество человек в компании.
import math as m
n = int(input())
s = n / 4
print(m.ceil(s))
# Парты
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Программа получает на вход три натуральных числа:количество учащихся в каждом из трех классов(числа не превышают 1000)
import math as m
a = int(input())
b = int(input())
c = int(input())
print(m.ceil(a / 2) +
      m.ceil(b / 2) +
      m.ceil(c / 2))
# Ремонт
# Ваш любимый дядя – директор фирмы, которая делает евроремонты в офисах.
# В связи с финансово-экономическим кризисом, дядюшка решил оптимизировать свое предприятие.
# Давно ходят слухи, что бригадир в дядюшкиной фирме покупает лишнее количество стройматериалов,
# а остатки использует для отделки своей новой дачи.
# Ваш дядя заинтересовался,сколько в действительности банок краски необходимо для покраски стен в офисе длиной L метров,
# шириной – W и высотой – H, если одной банки хватает на 16м2 , а размерами дверей и окон можно пренебречь?
# Заказов много, поэтому дядя попросил написать программу, которая будет все это считать.
# Входные данные
# Программа получает на вход три натуральных числа L, W, H – длину, ширину и высоту офиса в метрах соответственно,
# каждое из которых не превышает 1000.
# Выходные данные
# Выведите на экран одно целое число – минимальное количество банок краски, необходимых для покраски стен в офисе.
import math as m
l, w, h = map(int, input().split())
p = ((l * h) + (w * h)) * 2
print(m.ceil(p/16))
