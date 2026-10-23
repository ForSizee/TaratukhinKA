#1
a = [2, 0, 4, 6, 0, 8]
s = sum(a) / len(a)
a = [s if x == 0 else x for x in a]
print(a)

#2
a = [-1, 2, -3, 4, -5, 6]
b = []
c = []
for i in (a):
    if i < 0:
        b.append(b)
    else:
        c.append(i)
print(a,b,c)

#3
a = [1, 12, 31, 4, 175, 6, 100, 11000]
b = []
for i in (a):
    if i < 15:
        b.append(i * 2)
    else:
        b.append(i)
print(b)
from audioop import reverse

#4
a = [1,2,3,4,5,6,7,8]
b = []
for i in (a):
    if i % 2 != 0:
        b.append(i)

if not b:
    print("Массив пуст")
else:
    b = sorted(b)
    b.reverse()
    print(b)

#5
a = [1,2,2,4,5,5,7,7,9,10]
b = set(a)
print(list(b))

#6
a = input("Добавьте содержание массива из 10 эл-ов: ").split()
b = [int(x) for x in a]
summ = 0
for i in b:
    if i > 5:
        summ += i

print(summ)

#7
a = [7, 4, 6, 1, 9, 5]

min_i = a.index(min(a))
max_i = a.index(max(a))

a[min_i], a[max_i] = a[max_i], a[min_i]

print(a)

#8
a = [2, 0, 4, 6, 0, 8]
s = sum(a) / len(a)
a = [s if x == 0 else x for x in a]
print(a)

#9
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(A, B)
A, B = B, A
print(A)
print(B)

#10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 21, 33, 100]

print(a)

for i in range(len(a)):
    if a[i] < 10:
        a[i] = 0
    if a[i] > 20:
        a[i] = 1
    else:
        continue

print(a)

#11
F = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
C = []
for i in F:
    if i % 2 == 0 and i < 10:
        C.append(i)
if not C:
    print("В массиве нет эл-ов")
else:
    print(C)

#12
a = [7, 4, 6, 1, 9, 5]

min_i = a.index(min(a))
max_i = a.index(max(a))

a[min_i], a[max_i] = a[max_i], a[min_i]

print(a)

#13
a = [1, 12, 31, 4, 175, 6, 100, 11000]
b = []
for i in (a):
    if i < 15:
        b.append(i * 2)
    else:
        b.append(i)
print(b)

#14
a = input("Добавьте содержание массива из 10 эл-ов: ").split()
a = [int(x) for x in a]

s = sum(a) / len(a)

for i in range(len(a)):
    if a[i] > s:
        a[i] = 1
print(a)
#15
a = [1,2,3,4,5,6,7,8]
b = []
for i in (a):
    if i % 2 != 0:
        b.append(i)

if not b:
    print("Массив пуст")
else:
    b = sorted(b)
    b.reverse()
    print(b)