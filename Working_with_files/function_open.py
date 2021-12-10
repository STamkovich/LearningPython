# Чтение и запись данных. Функция open

# Будем работать с файлом формата .txt -  тоесть блокнот
# Для того чтобы открыть файл нужно сначала создать его.
# Создайте файл с расширением .txt и назовите его как угодно –
# Я назвал его test.txt, для того чтобы работать с этим файлом нужно его открыть в нашем коде.
# Для этого есть фунция Open
# Откроем переменную file:
# у вас вместо test.txt ваше название файла.
file = open('holy')
# Теперь мы можем работать с этой переменной file
# И первоем что мы можем сделать это прочитать содержимое блокнота – print(file.read())
# Если у вас в блокноте была кириллица и файл выдал всякую белеберду то сделайте так:
# = open('holy.txt', encoding='utf-8')
print(file.read())
# теперь всё должно заработать!
# Следующий метод print(file.readline()) – считывает одну линию.
# Файл можно обойти циклом for.
for line in file:
    print(line)  # – Будет считывать по одной линии

    # Для того чтобы считывать по словам:
    # for line in file:
    for letter in line:
        print(letter)  # – считывает по словам.

# Для того чтобы что-то записать в файл. Нужно сделать так:
file = open('test', 'w')  # – ‘w’ это мод write.

# По умолчанию там ‘r’ – read
file = open('test', 'w')

file.write('hello world')  # – обратите внимание что если у вас в файле до этого уже чтото было write удалит всё
# и напишет то что бы укажите.
#  что бы данные не затирались в файле нужно файл открыть в режиме "а" file = open('test', "а")
# Но при последующих вызовах он будет дописывать.
# Для того чтобы изначально дописывать используйте мод a
File = open('holy', 'a')

File.write('что')  # – теперь стираться не будет.

# Для того чтобы можно было одним модом и читать и записывать а раньше этого нельзя было делать используйте мод a+
# Также не забывайте закрывать файл file.close()
# Если у вас в работе с файлами будет ошибка то файл не закроется
# режим чтония и записи file = open('test', "а+")

file.close()  # его обязательно нужно вызывать после того как окончательно обработаете файл


#  в слцяае если файл не закрыть может произойти утечка памяти

# задачки
# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
# Учитывайте, что содержимое файла может быть как на русском языке, так и на английском
def file_read(file_name):
    file = open(file_name, encoding='utf-8')
    print(file.read())

# Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
# Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
# причем каждое число записывается  в отдельной строке
# Пимер: функция create_file_with_numbers(5) должна создать файл "range_5.txt" с содержимым
def create_file_with_numbers(n):
    file = open(f'/home/sergey/PycharmProjects/EgorovTaskPython/Working_with_files/range_{n}.txt', 'w')
    for i in range(1, n + 1):
        file.write(str(i) + '\n')

# Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое
# длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной,
# нужно вернуть слово, которое встречается последнее в тексте.
# При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.
# И также учитывайте, что слова в тестах будут как на русском языке, так и на английском
# Все возможные знаки пунктуации можно получить из модуля string
# from string import punctuation
from string import punctuation

def longest_word_in_file(file_name):
    f = open(file_name, encoding='utf-8')
    l = ''
    for i in f.read().split():
        i = i.strip()
        for j in i:
            if j in punctuation:
                i = i.replace(j, '')
        if len(i) >= len(l):
            l = i
    f.close()
    return l

