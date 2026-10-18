#1
n = int(input("Введите значение для переменной n: "))

i = 1
while i * i <= n:
    print(i * i, end="")
    i += 1

#2
n = int(input("Введите значение для переменной n не меньше 2: "))
digits_1 = []
for i in range(2, n + 1):
    if n % i == 0:
        digits_1.append(i)
print(min(digits_1))

#3
n = int(input("Введите значение для переменной n:"))

degree = 0
power = 1

while power * 2 <= n:
    power *= 2
    degree += 1

print(degree, power)

#4
x, y = map(float, input("Введите значения для переменных x и y через пробел: ").split())

day = 1

while x < y:
    x *= 1.1
    day += 1

print(day)

#5
count = 0

x = int(input('Введите значение для переменной x: '))

while x != 0:
    count += 1
    x = int(input("Введите значение для переменной x: "))

print(count)

#6
x = int(input("Введи значение для x: "))
y = []

while x != 0:
        y.append(x)
        x = int(input("Введи ещё одно значение для x или 0: "))
else:
    print(sum(y)/(len(y)))
        
#7
x = int(input("Введи значение для x: "))
y = []
cnt = 0

while x != 0:
        y.append(x)
        x = int(input("Введи ещё одно значение для x или 0: "))
else:
    for i in range(0, len(y) - 1):
        if y[i] < y[i + 1]:
            cnt += 1
    print(cnt)

#8
v = int(input("Введи значение для x: "))
s = []
cnt = 0

while v != 0:
        s.append(v)
        v = int(input("Введи ещё одно значение для x или 0: "))
else:
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
    print(cnt)
