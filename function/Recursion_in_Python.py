# Рекурсия в Python. Рекурсивная функция
# Рекурси - это ситуация внутри которой повторяется этаже ситуация
# В програмирования рекурсия - это когда функция вызывает саму себя
def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)


rec(1)


# первая часть ркурсии
# в рукерсии должно быть обязательное условие когда рекурсия должна остановится
# задача на рекурсию нахождения факториала
def factorial(x):
    if x == 1:
        return 1
    return factorial(x - 1) * x


print(factorial(4))
print(factorial(10))


# нахождение чисел фибаначи
def fib(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)


print(fib(5))
print(fib(10))
print(fib(6))


# с помощю рекурсии можно проверить является ли строка полиндромом
# полиндром это такая строка которая читается одинакова справа на лево и слева на право
# пример строка шалаш а так же пустая строка '' и 'a'
def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])


print(palindrom('ффв'))


def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]


s = input()
print(rec(s))


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return power(x, n - 1) * x


x = int(input())
n = int(input())
print(power(x, n))

a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level + 1)


rec(a)


# задачки
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Входные данные
# Программа принимает на вход натуральное число N (N ≤ 103).
# Во второй строке через пробел идут N целых чисел, по модулю не превосходящих 103 - элементы последовательности.
# Выходные данные
# Ваша задача вывести заданную последовательность в обратном порядке.
def recurs(n):
    if len(n) == 1:
        list2.append(n[0])
        return list2
    list2.append(n[-1])
    return recurs(n[:-1])


list2 = []
n = int(input())
list1 = input().split()
print(*recurs(list1))


# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи.
# Входные данные
# Программе поступает на вход целое число N (0 ≤ N ≤ 30) - порядковый номер числа Фибоначчи.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))


# Напишите функцию list_sum_recursive,
# которая принимает на вход список из целых чисел и возвращает сумму элементов переданного списка.
# Не забывайте, что реализовать это нужно при помощи рекурсии.
def list_sum_recursive(x):
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]
    return x[0] + list_sum_recursive(x[1:])


x = list(map(int, input().split()))
print(list_sum_recursive(x))


# Представьте, что у нас есть список целых чисел неограниченной вложенности.
# То есть наш список может состоять из списков, внутри которых также могут быть списки.
# Ваша задача превратить все это в линейный список при помощи функции flatten
# flatten([1, [2, 3, [4]], 5]) # вернет [1,2,3,4,5]
# flatten([1, [2,3], [[2], 5], 6]) # вернет [1,2,3,2,5,6]
# flatten([[[[9]]], [1,2], [[8]]]) # вернет [9,1,2,8]

def flatten(lst):
    new_lst = []
    for i in lst:
        if type(i) is int:
            new_lst.append(i)
        else:
            new_lst += flatten(i)
    return new_lst


print(flatten([[[[9]]], [1, 2], [[8]]]))  # вернет [1,2,3,4,5]


# Есть несколько типов сортировки, которые используют рекурсию. Одна из них называется сортировка слиянием
# Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию merge_sort,
# которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.
# Также для реализации функции merge_sort вам понадобится реализовать функцию merge_two_list.
# Функция merge_two_list должна принимать два отсортиванных по неубыванию списка,
# сливать их в один большой список также отсортированный по неубыванию (задача Слияние списков ) и возвращать его.
# Ваша задача написать только определение функций merge_sort и merge_two_list,
# при этом нельзя пользоваться встроенными сортировками в Python
def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


n = int(input())
mas = list(map(int, input().split()))
print(*merge_sort(mas))


# Быстрая сортировка - еще один вид сортировки, который использует рекурсию.
# Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию quick_sort,
# которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.
# Необходимо написать только определение функций quick_sort,
# при этом нельзя пользоваться встроенными сортировками в Python
# функция quick_sort должна выполнить сортировку
def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)


n = int(input())
mas = list(map(int, input().split()))
print(*quick_sort(mas))


# Дана строка, содержащая только английские буквы (большие и маленькие).
# Добавить символ ‘*’ (звездочка) между буквами (перед первой буквой и после последней символ ‘*’ добавлять не нужно).
# Входные данные
# Вводится строка ненулевой длины. Известно также, что длина строки не превышает 1000 знаков.
# Выходные данные
# Вывести строку, которая получится после добавления символов '*'.
# Примеры
# входные данные
# LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO
# выходные данные
# L*I*t*B*e*o*F*L*c*S*G*B*O*F*Q*x*M*H*o*I*u*D*D*W*c*q*c*V*g*k*c*R*o*A*e*o*c*X*O
def rec(s):
    if len(s) == 1:
        return s
    return s[0] + '*' + rec(s[1:])


s = 'LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO'
print(rec(s))

# Дана строка, содержащая только английские буквы (большие и маленькие) и открывающиеся скобки.
# Сформировать новую строку добавлением справа «зеркальной» строки с закрывающимися скобками.
# "(abc(def(g" -> "(abc(def(gg)fed)cba)"
# Входные данные
# Вводится строка ненулевой длины. Известно также, что длина строки не превышает 1000 знаков.
# Выходные данные
# Вывести строку, которая получится после "зеркальной" половины строки.
# Примеры
# входные данные
# (((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo
# выходные данные
# (((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s

# Чтобы предсказать судьбу человека,
# Если полученное число состоит более чем из одной цифры, операция повторяется, пока в числе не останется одна цифра.
# Затем по полученной цифре и числу операций, необходимых для преобразования числа в цифру нумеролог предсказывает
# судьбу человека. Нумеролог плохо умеет считать, а числа, с которыми он работает, могут быть очень большими.
# Напишите программу, которая бы делала все расчеты за него.
# Входные данные
# Входной файл INPUT.TXT содержит число N – время жизни человека в секундах (1 ≤ N ≤ 101000).
# Выходные данные
# В выходной файл OUTPUT.TXT выведите два числа через пробел: полученную цифру из числа N и число преобразований.

import os

#  Рекурсивный обход файлов
path = 'D:\\Programming Python'

print(os.listdir(path))
for i in os.listdir(path):
    print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))  # проверияем является ли элемент  папкой
    # print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i)) проверяем являетсья ли элемент файлом

import os

# Обход папки
path = 'D:\\Programming Python'


def obxodFile(path, level=1):
    print("level", level, 'content', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):  # проверяем есть ли папка в папке
            print('Спускаемся', path + '\\' + i)
            obxodFile(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)


obxodFile('D:\\Programming Python')