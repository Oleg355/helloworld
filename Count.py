a = int(input())
if a<1 or a>9999:
    print("Заданное число должно быть от 1 до 9999")
else:
    a = str(a)
    a = list(a)
    print(a.count('1'))
    print(a.count('2'))
    print(a.count('3'))
    print(a.count('4'))
