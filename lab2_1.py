import math

def expression (m):

    z = 1/(math.sqrt(m)+math.sqrt(2))

    return z 

def prime (n):
    if n > 1:
        for i in range(2,n):
            if n % i==0:
                return 0
   

    else:
        return 0
    return 1 

m = int(input("Введіть значення m: "))
while m<0:
    print("Число m може бути лише додатнім")
    m = int(input("Введіть значення m: "))
      
      
print ("Значення виразу z = ", expression(m))

n = int(input("Введіть число для перевірки на простоту: "))

if prime(n)==0:
    print("Число не є простим")
else:
    print("Число є простим")
