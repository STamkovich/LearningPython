# Экранированные (служебные символы) в Python
s = '''Hello 
world
hi
Bye'''
print(s)

print('hello\tworld')  # табуляция (4 пробела)

a = r'fff\tdsvvv\nfdfsfffsf\tcscscsd\t'  # помощю (R) отключаем все служебные символы
print(a)
print('/\_/\\\n>^,^<\n / \\\n(|_|)_/')
#   /~~~\
#  //^ ^\\
# (/(_*_)\)
# _/''*''\_
# (/_)^(_\)
print('  /~~~\\\n //^ ^\\\\\n(/(_*_)\\)\n_/\'\'*\'\'\\_\n(/_)^(_\\)')