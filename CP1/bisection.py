import math

r = 1.4274487577988

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
    return (math.cos(x)**2) + (2/35) * math.cos(x) - (1/35)

def g(x):
    return (math.cos(x)**2) - (2/7) * math.cos(x) + (1/49)

a = 0
b = 2
a_1 = 0
b_1 = 1.6
a_2 = 1.6
b_2 = 2
eps = 1e-4
eps = 1e-5
eps = 1e-5
# Викликаємо функцію MDihotom
print("MDihotom f(x) 1 проміжок: \t", MDihotom(f, a_1, b_1, eps))
print("MDihotom f(x) 2 проміжок: \t", MDihotom(f, a_2, b_2, eps))
# Викликаємо функцію MHord
print("MHord f(x) 1 проміжок:    \t", MHord(f, a_1, b_1, eps))
print("MHord f(x) 2 проміжок:    \t", MHord(f, a_2, b_2, eps))
# Викликаємо функцію Msecant
print("Msecant f(x) 1 проміжок: \t", Msecant(f, a_1, b_1, eps))
print("Msecant f(x) 2 проміжок: \t", Msecant(f, a_2, b_2, eps))

# Викликаємо функцію MDihotom
print("MDihotom g(x):\t", MDihotom(g, a, b, eps))
# Викликаємо функцію MHord
print("MHord g(x):   \t", MHord(g, a, b, eps))
# Викликаємо функцію Msecant
print("Msecant g(x): \t", Msecant(g, a, b, eps))












def f(x):
    return (math.sin(x))**2 + (5/6)*math.sin(x) + 1/6

def g(x):
    return (math.sin(x))**2 + (2/3)*math.sin(x) + 1/9



a1 = -1
b1 = -0.429775

a2 = -0.429775
b2 = 0


eps1=10**-4
eps2=10**-5
eps3=10**-6

















