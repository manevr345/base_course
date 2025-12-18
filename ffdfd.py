s = int(input())
s = (s - 21) // 10
n = 1
while s >= 0:
     n = n * 2
     s = s - n
print(n)

