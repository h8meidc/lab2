import math

from module import prime


def expression(m):

    z = 1 / (math.sqrt(m) + math.sqrt(2))

    return z


m = int(input("Введіть значення m: "))
while m < 0:
    print("Число m може бути лише додатнє")
    m = int(input("Введіть значення m: "))

print("Значення виразу z = ", expression(m))

n = int(input("Введіть число для перевірки на простоту: "))

if prime(n) == 0:
    print("Число не є простим")
else:
    print("Число є простим")
