num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))

if num2 != 0 and num1 % num2 == 0 :
    print(f"Число делится нацело Частное: {num1 / num2}")
elif num2 != 0 and num1 % num2 != 0:
    print(f"Число не делится нацело Частное: {num1 / num2} Остаток: {num1%num2}")
else:
    print("Ошибка!")
