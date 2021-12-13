# 10.5 Функция zip python
# zip(iter[,itr2 [...]]) --> zip object

a = [5, 6, 7, 8]

b = [100, 200, 300, 40]
# обращаемся в цикле for к элементам обоих списков которые стоят на одинаковых индексах

# for i in range(4):   весь этот код можно заменить одним вызовам функции zip
# print(a[i],b[i])

rez = zip(a, b)
print(rez)  # <zip object at 0x7f62c4e68980>
print(list(rez))  # [(5, 100), (6, 200), (7, 300), (8, 40)]
# функция zip сама определяет длину последовательности
# в функции zip нет ограничений на количество итерабельных последовательностей
# над итераторами нельзя находить длину итератора
# нельзя получать индекс
for i in zip(a, b):  # итератор можно обойти только один раз
    print(i)

# переменную rez можно обернуть в список
rez = list(zip(a, b))
print(rez)  # [(5, 100), (6, 200), (7, 300), (8, 40)]
# а список в свою очередь можно обходить в цикле for сколько угодно раз
c = 'hel'
rez = list(zip(a, b, c))
print(rez)  # [(5, 100, 'h'), (6, 200, 'e'), (7, 300, 'l')]
# количество в выводе кортежей определяется по минимальной длине всех коллекций которые участвуют в функции zip
for t1, t2, t3 in zip(a, b, c):  # делаем в цикле множественное присвоение
    print(t1, t2, t3)   # 5 100 h
                        # 6 200 e
                        # 7 300 l
# так же можно из результата работы функции zip  обратно получить наши списки
rez = zip(a, b, c)
# для этого создаём три переменные и присваиваем результат работы нашей zip и передаём нашу переменную со звёздочкой *
coll, coll2, coll3 = zip(*rez)
print(coll, coll2, coll3)  # (5, 6, 7) (100, 200, 300) ('h', 'e', 'l')