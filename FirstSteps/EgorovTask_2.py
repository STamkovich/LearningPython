                                                #  Деление нацело и деление по остатку

# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа
x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
e = a + b + c
print(e)

# Дележ яблок - 1
# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Программа получает на вход сперва число n, а потом k.
n = int(input())
k = int(input())
x = k // n
print(x)

# У вас есть N рублей и вы хотите купить максимальное количество кроссовок по цене R рублей.
# Сколько кроссовок Вы можете себе купить? На вход программе поступают 2 положительных целых числа N, R
n = int(input())
r = int(input())
s = n // r
print(s)

# У Олега в банке есть n евро. Он хочет снять всю сумму наличными. Номиналы еврокупюр равны 1, 5, 10, 20, 100.
# Какое минимальное число купюр должен получить Олег после того, как снимет все деньги? На вход программе поступает одно
# положительные целое число n.
n = int(input())
a = n // 100
b = n % 100 // 20
c = n % 100 % 20 // 10
d = n % 100 % 20 % 10 // 5
f = n % 100 % 20 % 10 % 5 // 1
print(a+b+c+d+f)
#  Электронные часы - 1
# Дано число n.С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в
# этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках
n = int(input())
print(((n // 60) % 24), n % 60)

# Дано целое число n. Выведите следующее за ним четное число.
# Задачу необходимо решить целочисленными операциями без использования условных операторов и\или циклов.
n = int(input())
print(n % 2 + n)

n = 5
a = n + 2
b = n % 2
c = a - b
print(c)

# Электронные часы - 2
# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне
# от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
# Программа получает на вход число n - количество секунд, которое прошло с начала суток.
# Выведите показания часов, соблюдая формат.
n = int(input())
h = (n // 3600) % 24
m = (n // 60) % 60
s = n % 60
print(str(h), str(m).rjust(2, '0'), str(s).rjust(2, '0'), sep=':')

