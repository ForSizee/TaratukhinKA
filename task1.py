#1
print("Курс Основы программирования начался")

#2
print((16823 * 12302) % 3092)

#3
age = input("Введите значение переменой age: ")
name = input("Введите значение переменой name: ")
age = int(age)

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
seconds = input("Введите значение переменой seconds: ")
seconds = int(seconds)

days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds_left = seconds % 60

print(days, "дн.", hours, "ч.", minutes, "мин.", seconds_left, "сек.")

#5
n = input("Введите значение для переменной n: ")
n = int(n)

result = n + n**2 + n**3 + n**4 + n**5

print(result)


#6
x = input("Введите значение переменой x: ")
y = input("Введите значение переменой y: ")
x = int(x)
y = int(y)

x, y = y, x

print("x =", x)
print("y =", y)

#7
number = 10

if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")