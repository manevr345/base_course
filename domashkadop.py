print("Введите коэф a, b, c чтобы нерешить уравнение вида 0 = a * x**2 + b * x + c")

a = float(input("Введите коэф. a: "))
b = float(input("Введите коэф. b: "))
c = float(input("Введите коэф. c: "))

Dis = b ** 2 - 4 * a * c

if Dis > 0:
    print(f"x1:{(-1*b + Dis**0.5)/(2 * a)} ")
    print(f"x2:{(-1*b - Dis**0.5)/(2 * a)} ")
elif Dis == 0:
    print(f"x = {(-1*b) / (2*a)}")
else:
    print("нет решений :(")
