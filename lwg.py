#1
print("Курс Основы программирования начался")

#2
print((16823 * 12302) % 3092)

#3
age = 17
name = "Кирилл"

if age >= 16:
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")

if age > 0 and age < 75:
    print("Возраст находится в допустимом диапазоне")
else:
    print("Возраст находится вне допустимого диапазона")

if name != "Иван":
    print("Поступающего зовут не Иван")
else:
    print("Поступающего зовут Иван")

if age < 16:
    print("Осталось учиться в школе:", 16 - age, "лет")

#4
seconds = 100000

days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds_left = seconds % 60

print(days, "дн.", hours, "ч.", minutes, "мин.", seconds_left, "сек.")

#5
n = "2"
n = int(n)

result = n + n2 + n3 + n4 + n5

print(result)


#6
x = 10
y = 20

x, y = y, x

print("x =", x)
print("y =", y)

#7
number = 10

if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")