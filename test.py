#!/usr/bin/python3

import sys

try:
    n = int(input("Введите целочисленное число от 1 до 100: ").strip())
except ValueError:
    print("Ошибка! Вы ввели не целочисленное число!")
    sys.exit()
finally:
    if 1 < n > 100:
        print("Число должно быть от 1 до 100!!")
        sys.exit()
if n % 2 != 0:          # если нечетное сразу пишем "Weird"
    print("Weird")      
elif 2 <= n <= 5:      # если четное и между 2 и 5 пишем "Not Weird"
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

