# Дано катети прямокутного трикутника a і b. Знайти його гіпотенузу c і периметр
# P: c=(a2+b2)1/2, P=a+b+c.
a = int(input('Введіть один катет'))
b = int(input('Введіть один катет'))

c = (a**2 + b**2)**(1/2)

P = a + b + c

print(c, P)