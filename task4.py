#1
def dox():
    A = int(input("Введите значение для переменной A: "))
    B = int(input("Введите значение для переменной B: "))

    if A > B:
        print("A должно быть меньше или равно B, ещё раз")
        dox()
    else:
        print(list(x for x in range(A, B + 1)))
dox()

#2
A = int(input("Введите значение для переменной A: "))
B = int(input("Введите значение для переменной B: "))

if A < B:
    print(list(x for x in range(A, B + 1)))
else:
    print(list(x for x in range(A, B - 1, -1)))

# #3
def dox_1():
    A = int(input("Введите значение для переменной A: "))
    B = int(input("Введите значение для переменной B: "))

    if A <= B:
        print("A должно быть больше B, ещё раз")
        dox_1()
    else:
        print(list(x for x in range(A, B - 1, -1) if x % 2 == 0))
dox_1()

#4
def dox_2():
    n = int(input("Введите количество чисел: "))
    digits_1 = list(map(int, input(f"Введите {n} чисел(ла), например(1 2 4): ").split()))
    if len(digits_1) == n:
        print(sum(digits_1))
    else:
        print("Вводите то количество чисел, которое указали раньше, ещё раз")
        dox_2()
dox_2()

#5
n = int(input("Введите значение для переменной n: "))
s = 0

for i in range(1, n + 1):
    s += i ** 3
print(s)

#6
n = int(input("Введите значение для переменной n: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i
print(factorial)

# 7
import math

n = int(input("Введите значение для переменной n: "))
sum = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    sum += factorial

print(sum)

# 8
def gg():
    n = int(input("Введите значение для переменной n <= 9: "))
    if n <= 9:
        for i in range(1, n + 1):
            for _ in range(1, i + 1):
                print(_, end="")
    else:
        print("Вводите n <= 9: ")
        gg()
gg()

# 9
n = int(input("Введите значание для переменной n: "))

a = 0
b = 1
s = 0

for i in range(n):
    s += a
    a, b = b, a + b
print(s)

# 10
n, k = map(int, input("Введите значение для переменной n и k через пробел: ").split())

a = 0
b = 1
s = 0

for i in range(1, k + n):
    if i >= k:
        s += a
    a, b = b, a + b
print(s)