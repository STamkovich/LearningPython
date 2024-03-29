# Вложенный оператор if
a = 35
if a % 5 == 0:
    if 9 < a < 100:
        print(1)
        print(2)
    else:
        print(3)
        print(4)
else:
    if a % 2 == 0:
        print(5)
        print(6)
    else:
        print(7)
        print(8)
print("end")

a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
print("end")

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

a = int(input())
if a % 4 == 0:
    print("ost 0")
else:
    if a % 4 == 1:
        print("ost 1")
    else:
        if a % 4 == 2:
            print("ost 2")

# Задачки
# В данной задаче необходимо сравнить два целых числа A и B. Они поступают на вход программе отдельно в каждой строке.
# Ваша задача вывести символ "<", если A меньше B, ">", если A больше B и "=", если A=B.
a = int(input())
b = int(input())
if a < b:
    print("<")
else:
    if a > b:
        print(">")
    else:
        if a == b:
            print("=")

# Даны три целых числа, каждое записано в отдельной строке.
# Нужно вывести значение наибольшего из данных чисел
# # Примечание: используйте только условный оператор, функцией max пользоваться нельзя
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

# На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму.
# Петя не знал, сколько гостей придет на его день рождения, поэтому вынужден был разработать алгоритм,
# согласно которому он сможет быстро разрезать торт на N равных частей.
# Следует учесть, что разрезы торта можно производить как по радиусу, так и по диаметру.
# Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.
# Входные данные
# Программа получает на вход натуральное число N – число гостей, включая самого виновника торжества
# Выходные данные
# Выведите минимально возможное число разрезов торта.
a = int(input())
if a % 2 == 0:
    print(int(a / 2))
if a != 1 and a % 2 != 0:
    print(a)
if a == 1:
    print(0)

# В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить:
# на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
# Входные данные
# Размеры зарплат всех сотрудников вводятся в одну строку через пробел. Каждая заработная плата – это натуральное число,
# не превышающее 105. И гарантируется ,что все зарплаты различны
# Выходные данные
# Необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.
a, b, c = map(int, input().split())
if a > b > c:
    print(a - c)
else:
    if a > c > b:
        print(a - b)
    else:
        if a < b < c:
            print(c - a)
        else:
            if c > a > b:
                print(c - b)
            else:
                if b > a > c:
                    print(b - c)
                else:
                    if b > c > a:
                        print(b - a)

# Маленький Петя очень любит подарки. Его мама подарила ему на день рождения две строки равной длины,
# состоящие из больших и маленьких букв латинского алфавита. Теперь Петя хочет сравнить эти строки лексикографически.
# При этом регистр букв значения не имеет, то есть большая буква считается эквивалентной соответствующей маленькой букве
# Помогите Пете выполнить сравнение.
# Входные данные
# В каждой из первых двух строк записано по одной подаренной строке. Длина строк находится в пределах от 1 до 100
# включительно. Гарантируется, что строки имеют одинаковую длину,
# а также состоят из больших и маленьких букв латинского алфавита.
# Выходные данные
# Если первая строка меньше второй, выведите «-1». Если вторая строка меньше первой, выведите «1». Если строки равны,
# выведите «0». Учтите, что регистр букв не учитывается при сравнении.
a = input().lower()
b = input().lower()
if a < b:
    print(-1)
else:
    if b < a:
        print(1)
    else:
        print(0)

# Кнопочные гонки
# Двое решили посоревноваться в набирании текстов на сайте «Кнопочные гонки».
# Во время соревнования необходимо ввести текст из s символов.
# Первый участник набирает один символ за v1 миллисекунд и имеет пинг t1 миллисекунд.
# Второй участник набирает один символ за v2 миллисекунд и имеет пинг t2 миллисекунд.
# При соединении с пингом (задержкой) в t миллисекунд соревнование проходит для участника следующим образом:
# Ровно через t миллисекунд после начала соревнования участник получает текст, который необходимо ввести.
# Сразу после этого он начинает вводить этот текст.
# Ровно через t миллисекунд после того, как он перепечатал весь текст, сайт получает информацию об этом.
# Победителем в соревновании является тот участник, информация об успехе которого пришла раньше.
# Если информация пришла от обоих участников одновременно, считается, что произошла ничья.
# По данной длине текста и информации об участниках, определите исход игры.
# Входные данные
# Первая строка содержит пять целых чисел s, v1, v2, t1, t2  — количество символов в тексте,
# скорость набора текста первым участником, скорость набора текста вторым участником,
# пинг первого участника и пинг второго участника.
# Выходные данные
# Если выиграет первый участник, выведите «First». Если выиграет второй участник, выведите «Second».
# В случае ничьей выведите «Friendship».
s, v1, v2, t1, t2 = map(int, input().split())
T1 = (s * v1) + t1 * 2
T2 = (s * v2) + t2 * 2
if T1 < T2:
    print("First")
if T1 > T2:
    print("Second")
if T1 == T2:
    print('Friendship')

# При игре в "Города" игроки по очереди называют названия городов так,
# чтобы первая буква каждого нового слова совпадала с последней буквой предыдущего.
# При этом считают, что если последняя буква предыдущего слова — мягкий знак,
# то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.
# Напишите программу, которая считывает подряд две строки, после чего выводит «Good»,
# если последний символ первой строки совпадает с первым символом второй (с учётом правила про мягкий знак),
# и «Bad» в противном случае.
a = input().lower()
b = input().lower()
if a[-1] == b[0]:
    print('Good')
else:
    if a[-1] == 'ь' and a[-2] == b[0]:
        print('Good')
    else:
        print('Bad')
