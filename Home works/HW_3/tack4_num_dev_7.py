# Программа по ввыводу из массива B чисел от 66 до 9999 кратных 7 в список А

a = []
b = [i for i in range(66, 10000)]
for x in b:
    if x % 7 == 0:
        a.append(x)
print (a)

