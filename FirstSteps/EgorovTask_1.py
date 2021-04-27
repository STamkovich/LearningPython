                                        # Функция input, print

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
s = int(input("Введите общее число сделаных журавликов"))
a = s // 6
b = (a+a)*2
print(a, b, a)

# Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров.
# Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера.
# Также известно, что стоимость карандаша составляет 3 рубля. Требуется определить общую стоимость покупки.
x, y, z = map(int, input().split())
print(x*3+y*5+z*12)

# Известно, что на обработку одного квадратного метра панели требуется 1г сульфида.
# Всего необходимо обработать N прямоугольных панелей размером A на B метров.
# Вам необходимо подсчитать, сколько всего сульфида необходимо на обработку всех панелей.
# И не забудьте, что панели требуют обработки с обеих сторон.
# На вход программе подаются 3 положительных числа N,A,B
c, a, b, = map(int, input().split())
print(c*a*b*2)

# Напишите программу, которая вычисляет средний балл ученика за решение четырех задач по введенным оценкам
# (числа от 2 до 5).
a, b, c, d = map(int, input().split())
e = a+b+c+d
print(e/4)

# Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя точками),
# заданного двумя значениями x1 и x2 (вещественные числа).
x1, x2 = map(float, input().split())
rez = abs(x2-x1)
print(rez)

# Бандиты Гарри и Ларри отдыхали на природе. Решив пострелять,
# они выставили на бревно несколько банок из-под кока-колы (не больше 10).
# Гарри начал простреливать банки по порядку, начиная с самой левой, Ларри — с самой правой.
# В какой-то момент получилось так, что они одновременно прострелили одну и ту же последнюю банку.
# Гарри возмутился и сказал, что Ларри должен ему кучу денег за то, что тот лишил его удовольствия прострелить
# несколько банок. В ответ Ларри сказал, что Гарри должен ему еще больше денег по тем же причинам.
# Они стали спорить кто кому сколько должен, но никто из них не помнил сколько банок было в начале,
# а искать простреленные банки по всей округе было неохота. Каждый из них помнил только, сколько банок прострелил он саm
# Определите по этим данным, сколько банок не прострелил Гарри и сколько банок не прострелил Ларри.
a, b = map(int, input().split())
c = (a + b - 1)
print(c - a, c - b)

# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы,
# минуты и секунды для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого.
# Определите, сколько секунд прошло между двумя моментами времени.
# Входные данные
# Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа,
# задающих второй момент времени.
# Выходные данные
# Выведите число секунд между этими моментами времени.
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
ra = ((a - x) * 3600)
rb = ((b - y) * 60)
rc = (c - z)

print(abs(ra + rb + rc))

# Петя учится в школе и очень любит математику. Уже несколько занятий они с классом проходят арифметические выражения.
# На последнем уроке учительница написала на доске три положительных целых числа a, b, c. Задание заключалось в том,
# чтобы расставить между этими числами знаки операций '+' и '*', а также, возможно, скобки. Значение получившегося
# выражения должно быть как можно больше. Рассмотрим пример: пусть учительница выписала на доску числа 1, 2 и 3.
# Вот некоторые варианты расстановки знаков и скобок:
# 1+2*3=7
# 1*(2+3)=5
# 1*2*3=6
# (1+2)*3=9
# Обратите внимание на то, что знаки операций можно вставлять только между a и b, а также между b и c,
# то есть нельзя менять числа местами. Так, в приведенном примере нельзя получить выражение (1+3)*2.
# Легко убедиться, что максимальное значение, которое можно получить, — это 9.
# Ваша задача — по заданным a, b и c вывести, какое максимальное значение выражения можно получить.
# Входные данные
# Во входных данных записаны три целых числа a, b и c, каждое в отдельной строке  (1≤a,b,c≤10).
# Выходные данные
# Выведите максимальное значение выражения, которое можно получить.
a = int(input())
b = int(input())
c = int(input())
e1 = a+b*c
e2 = a*(b+c)
e3 = (a*b*c)
e4 = (a+b)*c
e5 = a + b + c
print(max(e1, e2, e3, e4, e5))
# На вход поступают три целых числа - стороны треугольника.
# Необходимо вывести True, если данные стороны образуют прямоугольный треугольник, в противном случае - False.
#  a2 + b2 = c2, где a, b — катеты, с — гипотенуза.
a, b, c = map(int, input().split())
print((a ** 2 == b ** 2 + c ** 2 or
       (b ** 2 == a ** 2 + c ** 2 or
        (c ** 2 == b ** 2 + a ** 2))))

