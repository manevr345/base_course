x0 =10 # Переменная в глобальной области видимости
def move(t):
    u = 30
    x = x0 + u*t #переменные в локальной области
    return x
print(move(3))
a = 'Good'
def sora2():
    a = 'Bad'
    print(a)
sora2()
print(a)