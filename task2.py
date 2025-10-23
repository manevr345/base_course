a1 = float(input())
d = float(input())
n = int(input())
an = 0
for i in range(n):
    an = a1 * (d**(i))
    print(an, end = " ")
