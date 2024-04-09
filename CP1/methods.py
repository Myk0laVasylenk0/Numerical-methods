import math

# істинні значення коренів на проміжку [-1, 0]

r1 = -0.52359877
r2 = -0.33983690

def MDihotom(f, a, b, eps, r):
    while (abs(b-a)) > eps:
        x = (a + b) / 2
        print(f"{x}, {abs(r-x)}", sep="\t")
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return (a + b) / 2


def MHord(f, a, b, eps, r):
    x = a - f(a)*(b-a)/(f(b)-f(a))
    while abs(f(x)) > eps:
        x = a - f(a)*(b-a)/(f(b)-f(a))
        print(f"{x}, {abs(r-x)}", sep="\t")
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return x


def Msecant(f, a, b, eps, r):
  while True:
    if abs(f(b)) < eps:
      return b
    x_next = b - f(b) * (b - a) / (f(b) - f(a))
    print(f"{x_next}, {abs(r-x_next)}", sep="\t")
    a, b = b, x_next
  return b

# Приклад використання:
# Визначимо функцію f(x), початковий інтервал [a, b], та точність eps

def f(x):
    return (math.sin(x)**2) + (5/6) * math.sin(x) + (1/6)

def g(x):
    return (math.sin(x)**2) + (2/3) * math.sin(x) + (1/9)

a = -1
b = 0
a_1 = -1
b_1 = -0.4297
a_2 = -0.4297
b_2 = 0

eps = 1e-5

# функція f(x)
# Викликаємо функцію MDihotom
print("MDihotom f(x) 1 проміжок: \t", MDihotom(f, a_1, b_1, eps, r1))
print("MDihotom f(x) 2 проміжок: \t", MDihotom(f, a_2, b_2, eps, r2))
# Викликаємо функцію MHord
print("MHord f(x) 1 проміжок:    \t", MHord(f, a_1, b_1, eps, r1))
print("MHord f(x) 2 проміжок:    \t", MHord(f, a_2, b_2, eps, r2))
# Викликаємо функцію Msecant
print("Msecant f(x) 1 проміжок: \t", Msecant(f, a_1, b_1, eps, r1))
print("Msecant f(x) 2 проміжок: \t", Msecant(f, a_2, b_2, eps, r2))

# функція g(x)
# Викликаємо функцію MHord
print("MHord g(x):   \t", MHord(g, a, b, eps, r2))
# Викликаємо функцію Msecant
print("Msecant g(x): \t", Msecant(g, a, b, eps, r2))