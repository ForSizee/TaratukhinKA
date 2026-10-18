#1
a = input("Введите строку: ")
words = a.split()
cnt = 0

for i in range(len(words)):
    if (words[i].lower())[0] == 'е':
        cnt += 1
print(cnt)

#2
a = input("Введите строку: ")
cnt = a.count(':')
a = a.replace(':', '%')
print(a)
print(cnt)

#3
a = input("Введите строку: ")
cnt = a.count('.')
a = a.replace('.', '')
print(a)
print(cnt)

#4
a = input("Введите строку: ")
cnt = a.lower().count('а')
a = a.replace('а', 'о').replace('А', 'О')
print(a)
print(cnt)
print(len(a))

#5
a = input("Введите строку: ")
print(a.lower())

#6
a = input("Введите строку: ")
cnt = a.lower().count('а')
a = a.replace('а', '').replace('А', '')
print(a, cnt)

#7
a = input("Введите строку: ")
n = len(a) // 2
a = a[0:n]
a = a.lower().replace('п', '*').replace('П', '*')
print(a)

#8
a = input("Введите строку: ")
words = a.split()
cnt = len(words)
print(cnt)

#9
a = input("Введите строку: ")
y = input("Введите слово: ")
words = a.lower().split()
y = y.lower()
print(words.count(f'{y}'))

#10
print(input("Введите строку: ").title())

#11
a = input("Введите строку: ")
cnt = 0
digits = []

for i in range(len(a)):
    if a[i] == 'н' or a[i] == 'Н':
        cnt += 1
    else:
        digits.append(cnt)
        cnt = 0
digits.append(cnt)

print(a.replace('!','.'))
print(max(digits))

#12
a = input("Введите строку: ").replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace("'","")\
    .replace('"','').split()
z = []
for i in range(0, len(a)):
    if a[i][-1] == 'я':
        z.append(a[i])
print(z)

#13
a = input("Введите строку: ")
donk = []

for i in range(0, len(a)):
    if a[i] == '(':
        for x in range(i + 1, len(a)):
            if a[x] != ')':
                donk.append(a[x])
            else:
                break
    else:
        continue
print(donk)

#14
a = input("Введите строку: ").replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace("'","")\
    .replace('"','').lower().split()
z1 = []
for i in range(0, len(a)):
    if a[i][-1] == 'я' or a[i][0] == 'а':
        z1.append(a[i])
print(z1)

#15
a = input("Введите строку: ").lower()
cnt = 0
for i in range(0, len(a)):
    if a[i] == 'т':
        cnt += 1
print(cnt)