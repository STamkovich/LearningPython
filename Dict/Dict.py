# Словари
# Словари(Ассоциативный список) - это неупорядоченная коллекция произвольных объектов с доступом по ключу
# первый способ создания словаря(САМЫЙ ПОПУЛЯРНЫЙ)
a = ['moskva', 'piter', 'penza']

d = {
    # key:value,
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}
print(d)
# второй способ создание словаря(пондобится функция dict)
r = dict(moskva=495, piter=812, penza=8412)  # такой способ используется если в качестве ключей используються строки
print(r)
# третий способ создания словаря
# нужен вложенный список
b = [['moskva', 495], ['piter', 812], ['penza', 84112]]
t = dict(b)
print(t)
# четвёртый способ создания словаря
q = dict.fromkeys(['a', 'b', 'c'], 100)
print(q)

k = {}
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d)
# ВАЖНОЕ!!!!
# КЛЮЧЁМ НЕ МОЖЕТ БЫТЬ ИЗМЕНЯЕМЫЙ ТИП ОБЪЕКТА
# в словаре обращение идёт по значению ключа
# добавления значения в словрь делается при помощи присвоения значения ключу
d[4] = 'four'
d[5] = 'five'
print(d)
# словарь относиться к изменяемы объектам
d[3] = 'три'
print(d)
# ПРИМЕР
person = {}
s = 'IVANOV IVAN Samara SGU  4 5 5 4 3 5'
s = s.split()
person['lastname'] = s[0]
person['firstname'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(s)
print(person)
# удаление элемента из словаря
# изпользуем функцию del затем написать имя словаря и какой ключ хотите удалить
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d)
del d[1]
print(d)
# Функции словаря
# функция len - она подсчитывает сколько у вас имеется пар ключ-значений в вашем словаре
print(len(d))
# функция in - проверяет есть ли в нашем словаре какой либо ключ
print(2 in d)
if 1 in d:
    print(d[1])
else:
    d[1] = 'one'
print(d)
# так как словарь является колецией то все его элементы можем обходить циклом for
for key in d:
    print(key, d[key])
# методы словарей
# метод d.clear - очищает весь словарь
d.clear()
# d.get - принимает должное значение ключа возвращет
# значения ключа если его найдёт если же нет то возвращает значвение None
print(d.get(6))
# метод  d.setdefault - принимает одно обязательное значения ключ если значения нет он его сам создаёт ключ
# а значение будет None но через запятую можно передать значение ключу которого нет
print(d.setdefault(2, 'seven'))
# метод pop ему передаём значение ключа он вернёт вам значение и удалит его из словаря
print(d.pop(2))
# метод d.popitem удаляет случайные значения из словаря и возвращает пару
print(d.popitem())
# метод d.keys можем получеть значение всех ключей словаря
print(d.keys())
for key in d.keys():
    print(key)
# метод d.values можем получеть все значение словаря
print(d.values())
for value in d.values():
    print(value)
# метод d.items он возвращает калекцию в которой содеражатся все пары
for key, value in d.items():
    print(key, value)
# задачки
# На вход программе поступает целое число n.
# Вам необходимо создать словарь, который будет включать в себя ключи от 1 до n,
# а значениями соответствующего ключа будет значение ключа в квадрате.
# В качестве ответа выведите полученный словарь
n = int(input())
d = {}
for i in range(1, n + 1):
    d.setdefault(i, i ** 2)
print(d)
# Напишите программу, которая печатает словарь alphabet,
# где ключи  - строчные английские символы, а значения - порядковые номера букв в алфавите.
# Начало вашего словаря должны быть таким {"a": 1, "b": 2 }
# В качестве ответа распечатайте ключи и значения данного словаря по алфавиту, каждую пару на новой строчке.
# Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
from string import ascii_lowercase

alphabet = {}
for i in range(len(ascii_lowercase)):
    alphabet.setdefault(ascii_lowercase[i], i + 1)
for key in alphabet.keys():
    print(key, alphabet[key])
# Есть два словаря, нужно их объединить в новый словарь rez и вывести его на экран
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d3 = {d1 | d2}
print(d3)
# Система регистрации
# В скором времени в Берляндии откроется новая почтовая служба "Берляндеск".
# Администрация сайта хочет запустить свой проект как можно быстрее, поэтому они попросили Вас о помощи.
# Вам предлагается реализовать прототип системы регистрации сайта
# Система должна работать по следующему принципу. Каждый раз, когда новый пользователь хочет зарегистрироваться,
# он посылает системе запрос name со своим именем. Если данное имя не содержится в базе данных системы,
# то оно заносится туда и пользователю возвращается ответ OK, подтверждающий успешную регистрацию.
# Если же на сайте уже присутствует пользователь с именем name,
# то система формирует новое имя и выдает его пользователю в качестве подсказки,
# при этом подсказка также добавляется в базу данных. Новое имя формируется по следующему правилу.
# К name последовательно приписываются числа, начиная с единицы (name1, name2, ...),
# и среди них находят такое наименьшее i, что namei не содержится в базе данных сайта.
# Входные данные
# В первой строке входных данных задано число n (1 ≤ n ≤ 105). С
# ледующие n строк содержат запросы к системе.
# Каждый запрос представляет собой непустую строку длиной не более 32 символов,
# состоящую только из строчных букв латинского алфавита.
# Выходные данные
# В выходных данных должно содержаться n строк — ответы системы на запросы:
# OK в случае успешной регистрации, или подсказку с новым именем, если запрашиваемое уже занято.
n = int(input())
dic = {}
for i in range(n):
    key = input()
    if key in dic:
        dic[key] += 1
        key = key + str(dic[key])
        dic.setdefault(key, i)
        print(key)
        dic[key] += 1
    else:
        dic.setdefault(key, i)
        print("OK")
        dic[key] = 0

#