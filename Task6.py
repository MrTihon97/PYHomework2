# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


number = float(input("Введите число: "))
w = int(number)
f = (number - w)
f = f * 10**(len(str(f))-2)
sum = 0
while w > 0:
    sum += w % 10
    w //= 10
while f > 0:
    sum += f % 10
    f //= 10
print(int(sum))

