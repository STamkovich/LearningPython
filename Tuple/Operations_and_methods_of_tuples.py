# 6.4 Кортежи (tuple). Операции и методы кортежей
# Кортеж - неизменяемая последовательность, обычно используемая для хранения разнопоточных объектов
# кортеж является итерабелной последовательностью
# кортежи являются упорядочной коллекцией
# кортеж имеет всего два метода index, count
# кортеж может в себе иметь изменяемые объекты
# кортеж имеет всего два метода index, count
# кортеж может в себе иметь изменяемые объекты
# кртежи занимают меньше места в памяти в отличии от списков
# картежи нужны вслучае когда вам необходими гарантировать неизменяемость объекта

# создание кортежа

a = (1, 2, 3, 4, 5)
a1 = 1, 'hello', 3, [2, 3, 5], 54, False, 5
print(a, type(a))
print(a1[1]) # обращение по интексу
a1[3].append(100)
print(a1)

#  следующий способ создать кортеж это использовать однаимённую функцию
b = tuple((1, 2, 3))
print(b, type(b))

# Операции которые поддерживает кортеж
len(a)
print(2 in a, 6 not in a)
print((a + b, b + a))
print(a * 4)
print(min(a), max(a))
print(sum(a))


c = [1, 'hello', 3, [2, 3, 5], 54, False, 5]
d = tuple([1, 'hello', 3, [2, 3, 5], 54, False, 5])
print(c.__sizeof__())
print(d.__sizeof__())
# __siseof__() этот метод измеряет сколько занимает места объект

# кортежи могут быть использованы в качестве ключей словаря

e = (1, 2, 3)
d = {a: 'hello'}
print(d)

# кортеж всегда можно преобразовать к списку  и потом обратно в кортеж

t = (1, 2, 3, 5)
t = list(t)
print(a, type(t))
t.append(100)
t.reverse()
t = tuple(t)
print(t)

for i in range(len(t)):
    print(a[i])


# задачки
# Допишите программу ниже,
# чтобы она вывела через пробел в одной строке значения самого маленького и самого большого элементов кортежа my_tuple.
my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781,
            759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791,
            631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933,
            -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278,
            867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472,
            -986, -964, -73, 29)

print(min(my_tuple), max(my_tuple))

# Допишите программу ниже, чтобы она вывела среднего арифметического всех нечетных элементов кортежа my_tuple.

my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781,
            759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791,
            631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933,
            -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278,
            867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472,
            -986, -964, -73, 29)

count = 0
count1 = 0

for i in my_tuple:
    if i // 2 == 0:
        continue
    else:
        count += i
        count1 += 1

sr = count / count1
print(sr)

